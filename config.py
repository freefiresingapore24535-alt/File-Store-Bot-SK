# ───────────────────────────────────────────
#   (©) TECH ZORO TAMIL — OFFICIAL BOT
#   Credits Must Stay • Thank You ♥
# ───────────────────────────────────────────

import logging
from logging.handlers import RotatingFileHandler

# ───────────────────────────────────────────
#   📦 BOT CONFIGURATION
#   (©) TECH ZORO TAMIL — PREMIUM BUILD
# ───────────────────────────────────────────
LOG_FILE_NAME = "bot.log"
PORT = '5010'
OWNER_ID = 5960133511

MSG_EFFECT = 5046509860389126442

SHORT_URL = "linkshortify.com" # shortner url 
SHORT_API = "" 
SHORT_TUT = "https://t.me/+fuhw3bZ97NgxMzE1"

# Bot Configuration
SESSION = "Zoro"
TOKEN = "8464041039:AAER0Ef7fRvHn8Du-F7zJOe5IgM50ckrjto"
API_ID = "22128383"
API_HASH = "7992b5c5c9c6d34276c3dce9e46ba879"
WORKERS = 5

# mongo db
DB_URI = "mongodb+srv://Rei061:Rei061@cluster0.pmn26.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "zoro"

# Force Subscription Channels [channel_id, request_enabled, timer_in_minutes]
FSUBS = [[-1001926236146, True, 10]]
# Database Channel (Primary)
DB_CHANNEL = -1002998057898
# Multiple Database Channels (can be set via bot settings)
# DB_CHANNELS = {
#     "-1002595092736": {"name": "Primary DB", "is_primary": True, "is_active": True},
#     "-1001234567890": {"name": "Secondary DB", "is_primary": False, "is_active": True}
# }
# Auto Delete Timer (seconds)
AUTO_DEL = 300
# Admin IDs
ADMINS = [6587671439]
# Bot Settings
DISABLE_BTN = True
PROTECT = False

# Messages Configuration
MESSAGES = {
    "START": "<b>›› ʜᴇʏ!!, {first} ~ <blockquote>ɪ ᴀᴍ ᴍᴀᴅᴇ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ғɪɴᴅ ᴡʜᴀᴛ ʏᴏᴜ aʀᴇ ʟᴏᴏᴋɪɴɢ ꜰᴏʀ.</blockquote></b>",
    "FSUB": "<b><blockquote>›› ʜᴇʏ ×</blockquote>\n  ʏᴏᴜʀ ғɪʟᴇ ɪs ʀᴇᴀᴅʏ ‼️ ʟᴏᴏᴋs ʟɪᴋᴇ ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ sᴜʙsᴄʀɪʙᴇᴅ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ʏᴇᴛ, sᴜʙsᴄʀɪʙᴇ ɴᴏᴡ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ғɪʟᴇs</b>",
    "ABOUT": "<b>›› ғᴏʀ ᴍᴏʀᴇ: @Sk_Anime_1 \n <blockquote expandable>›› ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/+AdcXPREPNEpkZmNl'>Cʟɪᴄᴋ ʜᴇʀᴇ</a> \n›› ᴏᴡɴᴇʀ: @Minato_Sencie\n›› ʟᴀɴɢᴜᴀɢᴇ: <a href='https://docs.python.org/3/'>Pʏᴛʜᴏɴ 3</a> \n›› ʟɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ ᴠ2</a> \n›› ᴅᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>Mᴏɴɢᴏ ᴅʙ</a> \n›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href='https://t.me/Minato_Sencie'>Cʟɪᴄᴋ ʜᴇʀᴇ</a> </b></blockquote>",
    "REPLY": "<b>For More Join - @Sk_Anime_1</b>",
    "SHORT_MSG": "<b>📊 ʜᴇʏ {first}, \n\n‼️ ɢᴇᴛ ᴀʟʟ ꜰɪʟᴇꜱ ɪɴ ᴀ ꜱɪɴɢʟᴇ ʟɪɴᴋ ‼️\n\n ⌯ ʏᴏᴜʀ ʟɪɴᴋ ɪꜱ ʀᴇᴀᴅʏ, ᴋɪɴᴅʟʏ ᴄʟɪᴄᴋ ᴏɴ ᴏᴘᴇɴ ʟɪɴᴋ ʙᴜᴛᴛᴏɴ..</b>",
    "START_PHOTO": "https://files.catbox.moe/pc7mr8.png",
    "FSUB_PHOTO": "https://files.catbox.moe/dpk0pi.jpg",
    "SHORT_PIC": "https://files.catbox.moe/9hb0wc.jpg",
    "SHORT": "https://files.catbox.moe/pc7mr8.png"
}

def LOGGER(name: str, client_name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
        f"[%(asctime)s - %(levelname)s] - {client_name} - %(name)s - %(message)s",
        datefmt='%d-%b-%y %H:%M:%S'
    )
    file_handler = RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
