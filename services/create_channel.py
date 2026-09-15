# # """
# # Yangi guruh uchun Telegram kanalni avtomatik yaratish xizmati.

# # Jarayon:
# #   1. userbot orqali yangi kanal (broadcast channel) yaratiladi
# #   2. Kanal uchun taklif havolasi (invite link) generatsiya qilinadi
# #   3. Asosiy Humo Kids bot kanalga a'zo sifatida qo'shiladi
# #   4. Botga to'liq admin huquqlari beriladi (post, tahrirlash, o'chirish va h.k.)

# import asyncio
# import logging

# from pyrogram.errors import FloodWait, UserAlreadyParticipant

# from config import settings
# from exceptions import ChannelCreationError
# from userbot_client import userbot

# logger = logging.getLogger(__name__)

# MAX_RETRIES = 3



# from pyrogram.types import ChatPrivileges

# async def create_channel_for_group(
#     title: str, description: str | None = None, _attempt: int = 1
# ) -> dict:
#     """Yangi kanal yaratadi va natijani lug'at (dict) sifatida qaytaradi.

#     Returns:
#         {"channel_id": int, "invite_link": str}

#     Raises:
#         ChannelCreationError: kanal yaratib bo'lmagan hollarda.
#     """
#     try:
#         async with userbot:
#             channel = await userbot.create_channel(
#                 title=f"Humo Kids | {title}",
#                 description=description or f"Humo Kids bog'chasi — {title} rasmiy kanali",
#             )
#             channel_id = channel.id
#             logger.info(f"Kanal yaratildi: '{title}' -> chat_id={channel_id}")

#             invite_link = await userbot.export_chat_invite_link(channel_id)

#             # Botga to'liq admin huquqlarini berish
#             await userbot.promote_chat_member(
#                 chat_id=channel_id,
#                 user_id=settings.bot_username,
#                 can_post_messages=True,
#                 can_edit_messages=True,
#                 can_delete_messages=True,
#                 can_invite_users=True,
#                 can_pin_messages=True,
#                 can_manage_chat=True,
#             )
#             logger.info(f"Bot '{settings.bot_username}' kanalga admin sifatida qo'shildi.")

#             return {"channel_id": channel_id, "invite_link": invite_link}

#     except FloodWait as e:
#         if _attempt >= MAX_RETRIES:
#             raise ChannelCreationError(
#                 f"FloodWait limitiga {MAX_RETRIES} marta duch kelindi, urinish to'xtatildi."
#             )
#         logger.warning(f"FloodWait: {e.value} soniya kutilmoqda (urinish {_attempt}/{MAX_RETRIES})")
#         await asyncio.sleep(e.value)
#         return await create_channel_for_group(title, description, _attempt=_attempt + 1)

#     except Exception as e:
#         logger.exception("Kanal yaratishda kutilmagan xatolik")
#         raise ChannelCreationError(str(e)) from e


#     # Botga to'liq admin huquqlarini berish
#     await userbot.promote_chat_member(
#              chat_id=channel_id,
#              user_id=settings.bot_username,
#              privileges=ChatPrivileges(
#                  can_post_messages=True,
#                  can_edit_messages=True,
#                  can_delete_messages=True,
#                  can_invite_users=True,
#                  can_pin_messages=True,
#                  can_manage_chat=True,
#              ),
#          )
#     logger.info(f"Bot '{settings.bot_username}' kanalga admin sifatida qo'shildi.")


"""
Yangi guruh uchun Telegram kanalni avtomatik yaratish xizmati.

Jarayon:
  1. userbot orqali yangi kanal (broadcast channel) yaratiladi
  2. Kanal uchun taklif havolasi (invite link) generatsiya qilinadi
  3. Botga to'liq admin huquqlari beriladi
"""
import asyncio
import logging

from pyrogram.errors import FloodWait
from pyrogram.types import ChatPrivileges

from config import settings
from exceptions import ChannelCreationError
from userbot_client import userbot

logger = logging.getLogger(__name__)

MAX_RETRIES = 3


async def create_channel_for_group(
    title: str, description: str | None = None, _attempt: int = 1
) -> dict:
    """Yangi kanal yaratadi va natijani lug'at (dict) sifatida qaytaradi.

    Returns:
        {"channel_id": int, "invite_link": str}

    Raises:
        ChannelCreationError: kanal yaratib bo'lmagan hollarda.
    """
    try:
        async with userbot:
            channel = await userbot.create_channel(
                title=f"Humo Kids | {title}",
                description=description or f"Humo Kids bog'chasi — {title} rasmiy kanali",
            )
            channel_id = channel.id
            logger.info(f"Kanal yaratildi: '{title}' -> chat_id={channel_id}")

            invite_link = await userbot.export_chat_invite_link(channel_id)

            # Botga to'liq admin huquqlarini berish
            await userbot.promote_chat_member(
                chat_id=channel_id,
                user_id=settings.bot_username,
                privileges=ChatPrivileges(
                    can_post_messages=True,
                    can_edit_messages=True,
                    can_delete_messages=True,
                    can_invite_users=True,
                    can_pin_messages=True,
                    can_manage_chat=True,
                ),
            )
            logger.info(f"Bot '{settings.bot_username}' kanalga admin sifatida qo'shildi.")

            return {"channel_id": channel_id, "invite_link": invite_link}

    except FloodWait as e:
        if _attempt >= MAX_RETRIES:
            raise ChannelCreationError(
                f"FloodWait limitiga {MAX_RETRIES} marta duch kelindi, urinish to'xtatildi."
            )
        logger.warning(f"FloodWait: {e.value} soniya kutilmoqda (urinish {_attempt}/{MAX_RETRIES})")
        await asyncio.sleep(e.value)
        return await create_channel_for_group(title, description, _attempt=_attempt + 1)

    except Exception as e:
        logger.exception("Kanal yaratishda kutilmagan xatolik")
        raise ChannelCreationError(str(e)) from e