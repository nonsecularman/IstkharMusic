import sys
import asyncio

if sys.platform != "win32":
    try:
        import uvloop
        uvloop.install()
    except ImportError:
        pass

from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config
from ..logging import LOGGER


class Istkhar(Client):
    def __init__(self):
        LOGGER(__name__).info("Starting Bot...")
        super().__init__(
            name="IstkharMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()

        self.id = self.me.id
        self.name = self.me.first_name
        self.username = self.me.username
        self.mention = self.me.mention

        # ===== SAFE LOG GROUP HANDLING =====
        try:
            await self.send_message(
                chat_id=config.LOG_GROUP_ID,
                text=(
                    f"<u><b>» {self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b></u>\n\n"
                    f"ɪᴅ : <code>{self.id}</code>\n"
                    f"ɴᴀᴍᴇ : {self.name}\n"
                    f"ᴜsᴇʀɴᴀᴍᴇ : @{self.username}"
                ),
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid) as e:
            LOGGER(__name__).error(
                "Log group/channel access failed (invalid ID or bot not added)."
            )
            LOGGER(__name__).error(f"Reason: {type(e).__name__}")
            LOGGER(__name__).error("Continuing WITHOUT log group to avoid crash.")

        except Exception as e:
            LOGGER(__name__).error(
                "Unexpected error while accessing log group/channel."
            )
            LOGGER(__name__).error(f"Reason: {type(e).__name__}")
            LOGGER(__name__).error("Continuing WITHOUT log group to avoid crash.")

        # ===== ADMIN CHECK (SAFE) =====
        try:
            member = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
            if member.status != ChatMemberStatus.ADMINISTRATOR:
                LOGGER(__name__).warning(
                    "Bot is not admin in log group. Logging may not work."
                )
        except Exception as e:
            LOGGER(__name__).warning(
                "Failed to verify admin status in log group."
            )
            LOGGER(__name__).warning(f"Reason: {type(e).__name__}")

        LOGGER(__name__).info(f"Music Bot Started as {self.name}")

    async def stop(self):
        await super().stop()
