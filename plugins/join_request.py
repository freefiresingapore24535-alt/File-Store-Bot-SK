from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest, ChatMemberUpdated
from pyrogram.enums import ChatMemberStatus

#===============================================================#

@Client.on_chat_join_request(filters.channel)
async def handle_join_request(client, join_request: ChatJoinRequest):
    user_id = join_request.from_user.id
    channel_id = join_request.chat.id
    channel_name = join_request.chat.title
    channel = client.fsub_dict.get(channel_id, [])
    
    is_banned = await client.mongodb.is_banned(user_id)
    if is_banned:
        return
    
    if channel:
        await client.mongodb.add_join_request(
            user_id,
            channel_id,
            getattr(join_request, 'id', None)
        )
        await client.mongodb.update_fsub_status(user_id, channel_id, "request_submitted")
        await client.mongodb.add_channel_user(channel_id, user_id)
        
        client.LOGGER(__name__, client.name).info(
            f"Join request recorded for user {user_id} in channel {channel_name}"
        )

#===============================================================#

@Client.on_chat_member_updated(filters.channel)
async def handle_member_update(client, chat_member_updated: ChatMemberUpdated):
    """Handle when users join or leave channels"""

    # SAFETY FIX → Ignore empty/incomplete updates
    if not chat_member_updated:
        return
    if not chat_member_updated.from_user:
        return
    if not chat_member_updated.chat:
        return
    if not chat_member_updated.new_chat_member:
        return  # <-- MAIN FIX (prevents crash)

    user_id = chat_member_updated.from_user.id
    channel_id = chat_member_updated.chat.id

    # Only process updates for fsub channels
    if channel_id not in client.fsub_dict:
        return
    
    old_status = (
        chat_member_updated.old_chat_member.status
        if chat_member_updated.old_chat_member
        else None
    )

    # SAFETY FIX → new_chat_member can be None
    new_member = chat_member_updated.new_chat_member
    new_status = getattr(new_member, "status", None)
    if new_status is None:
        return  # Ignore invalid update
    
    channel_name = client.fsub_dict[channel_id][0]

    # User joined the channel
    if new_status in {
        ChatMemberStatus.MEMBER,
        ChatMemberStatus.ADMINISTRATOR,
        ChatMemberStatus.OWNER
    }:
        await client.mongodb.update_fsub_status(user_id, channel_id, "joined")
        await client.mongodb.add_channel_user(channel_id, user_id)
        
        if await client.mongodb.has_submitted_join_request(user_id, channel_id):
            await client.mongodb.update_join_request_status(user_id, channel_id, "approved")
        
        client.LOGGER(__name__, client.name).info(
            f"User {user_id} joined channel {channel_name}"
        )
    
    # User left the channel
    elif old_status in {
        ChatMemberStatus.MEMBER,
        ChatMemberStatus.ADMINISTRATOR,
        ChatMemberStatus.OWNER
    } and new_status in {
        ChatMemberStatus.LEFT,
        ChatMemberStatus.BANNED
    }:
        await client.mongodb.update_fsub_status(user_id, channel_id, "left")
        await client.mongodb.remove_channel_user(channel_id, user_id)
        
        if await client.mongodb.has_submitted_join_request(user_id, channel_id):
            await client.mongodb.remove_join_request(user_id, channel_id)
        
        client.LOGGER(__name__, client.name).info(
            f"User {user_id} left channel {channel_name}"
        )
    
    # User was banned
    elif new_status == ChatMemberStatus.BANNED:
        await client.mongodb.update_fsub_status(user_id, channel_id, "banned")
        await client.mongodb.remove_channel_user(channel_id, user_id)
        
        if await client.mongodb.has_submitted_join_request(user_id, channel_id):
            await client.mongodb.remove_join_request(user_id, channel_id)
        
        client.LOGGER(__name__, client.name).info(
            f"User {user_id} was banned from channel {channel_name}"
        )
