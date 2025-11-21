# ───────────────────────────────────────────
#   🚀 MAIN LAUNCHER (TECH ZORO TAMIL)
#   Premium • Clean • Fast Boot Handler
# ───────────────────────────────────────────

import asyncio
from bot import Bot, web_app
from pyrogram import compose
from config import *

async def main():
    app = []

    # Initialize bot using config values
    app.append(
        Bot(
            SESSION,
            WORKERS,
            DB_CHANNEL,
            FSUBS,
            TOKEN,
            ADMINS,
            MESSAGES,
            AUTO_DEL,
            DB_URI,
            DB_NAME,
            API_ID,
            API_HASH,
            PROTECT,
            DISABLE_BTN
        )
    )

    await compose(app)


async def runner():
    await asyncio.gather(
        main(),
        web_app()
    )

asyncio.run(runner())
