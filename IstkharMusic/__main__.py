# ===== EVENT LOOP FIX (MUST BE AT TOP) =====
import asyncio

try:
    asyncio.get_running_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

# ===== अब safe है Pyrogram import =====
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from IstkharMusic import LOGGER, app, userbot
from IstkharMusic.core.call import Istkhar
from IstkharMusic.misc import sudo
from IstkharMusic.plugins import ALL_MODULES
from IstkharMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        return

    await sudo()

    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)

        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except Exception as e:
        LOGGER(__name__).warning(f"Ban load failed: {e}")

    await app.start()

    for all_module in ALL_MODULES:
        importlib.import_module("IstkharMusic.plugins" + all_module)

    LOGGER("IstkharMusic.plugins").info("Successfully Imported Modules...")

    await userbot.start()
    await Istkhar.start()

    try:
        await Istkhar.stream_call(
            "https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("IstkharMusic").error(
            "Please turn on the videochat of your log group/channel.\n\nStopping Bot..."
        )
        return
    except Exception as e:
        LOGGER("IstkharMusic").warning(f"Stream call issue: {e}")

    await Istkhar.decorators()

    LOGGER("IstkharMusic").info("-1002447776304")

    await idle()

    await app.stop()
    await userbot.stop()
    LOGGER("IstkharMusic").info("Stopping Istkhar Music Bot...")


if __name__ == "__main__":
    asyncio.run(init())
