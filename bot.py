# ======================================================================
# ████████╗███████╗ ██████╗██╗  ██╗
# ╚══██╔══╝██╔════╝██╔════╝██║ ██╔╝
#    ██║   █████╗  ██║     █████╔╝     (©) TECH ZORO TAMIL
#    ██║   ██╔══╝  ██║     ██╔═██╗     OFFICIAL FILE STORE BOT
#    ██║   ███████╗╚██████╗██║  ██╗
#    ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝
#
# 🔥 Premium Code Maintained by: TECH ZORO TAMIL
# 📌 Credits Must NOT Be Removed
# 📢 Telegram: t.me/TechZoroTamil
# ======================================================================

from aiohttp import web
from plugins import web_server

from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime
from config import LOGGER, PORT, OWNER_ID, SHORT_URL, SHORT_API, SHORT_TUT
from helper import MongoDB

version = "v1.0.0"


class Bot(Client):
    def __init__(self, session, workers, db, fsub, token, admins, messages, auto_del, db_uri, db_name, api_id, api_hash, protect, disable_btn):
        super().__init__(
            name=session,
            api_hash=api_hash,
            api_id=api_id,
            plugins={
                "root": "plugins"
            },
            workers=workers,
            bot_token=token
        )
        self.LOGGER = LOGGER
        self.name = session
        self.db = db
        self.fsub = fsub
        self.owner = OWNER_ID
        self.fsub_dict = {}
        self.admins = admins + [OWNER_ID] if OWNER_ID not in admins else admins
        self.messages = messages
        self.auto_del = auto_del
        self.protect = protect
        self.req_fsub = {}
        self.disable_btn = disable_btn
        self.reply_text = messages.get('REPLY', 'Do not send any useless message in the bot.')
        self.mongodb = MongoDB(db_uri, db_name)
        self.req_channels = []
        self.db_channels = {} 
        self.primary_db_channel = db  

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        try:
            restart_message = "<b>🔥 TECH ZORO TAMIL BOT RESTARTED 🔥\nYour bot is now alive! ⚡</b>"
            await self.send_message(chat_id=self.owner, text=restart_message)
        except Exception as e:
            pass

        self.username = usr_bot_me.username

    async def stop(self, *args):
        await super().stop()


async def web_app():
    app = web.AppRunner(await web_server())
    await app.setup()
    bind_address = "0.0.0.0"
    await web.TCPSite(app, bind_address, PORT).start()
