# """
# Guruh o'chirilganda unga bog'liq Telegram kanalni avtomatik o'chirish xizmati.
# """
# import asyncio
# import logging

# from pyrogram.errors import ChannelInvalid, FloodWait

# from exceptions import ChannelDeletionError
# from userbot_client import userbot

# logger = logging.getLogger(__name__)

# MAX_RETRIES = 3


# async def delete_channel_by_id(channel_id: int, _attempt: int = 1) -> None:
#     """Berilgan chat_id bo'yicha kanalni butunlay o'chiradi.

#     Raises:
#         ChannelDeletionError: kanalni o'chirib bo'lmagan hollarda.
#     """
#     try:
#         async with userbot:
#             await userbot.delete_channel(channel_id)
#             logger.info(f"Kanal o'chirildi: chat_id={channel_id}")

#     except ChannelInvalid:
#         # Kanal allaqachon mavjud emas — bu holatni xatolik deb hisoblamaymiz
#         logger.warning(f"Kanal topilmadi (allaqachon o'chirilgan bo'lishi mumkin): {channel_id}")
#         return

#     except FloodWait as e:
#         if _attempt >= MAX_RETRIES:
#             raise ChannelDeletionError(
#                 f"FloodWait limitiga {MAX_RETRIES} marta duch kelindi, urinish to'xtatildi."
#             )
#         logger.warning(f"FloodWait: {e.value} soniya kutilmoqda (urinish {_attempt}/{MAX_RETRIES})")
#         await asyncio.sleep(e.value)
#         await delete_channel_by_id(channel_id, _attempt=_attempt + 1)

#     except Exception as e:
#         logger.exception("Kanalni o'chirishda kutilmagan xatolik")
#         raise ChannelDeletionError(str(e)) from e


# """
# Guruh o'chirilganda unga bog'liq Telegram kanalni avtomatik o'chirish xizmati.
# """
# import asyncio
# import logging

# from pyrogram.errors import ChannelInvalid, FloodWait, PeerIdInvalid, RPCError

# from exceptions import ChannelDeletionError
# from userbot_client import userbot

# logger = logging.getLogger(__name__)

# MAX_RETRIES = 3


# async def delete_channel_by_id(channel_id: int, _attempt: int = 1) -> None:
#     """Berilgan chat_id bo'yicha kanalni butunlay o'chiradi.

#     Raises:
#         ChannelDeletionError: kanalni o'chirib bo'lmagan hollarda.
#     """
#     try:
#         chat_id_int = int(channel_id)
#         async with userbot:
#             # Pyrogram chatni taniy olishi uchun avval keshga chaqirib olamiz
#             try:
#                 await userbot.get_chat(chat_id_int)
#             except Exception as get_err:
#                 logger.warning(f"get_chat ogohlantirishi (davom etamiz): {get_err}")

#             await userbot.delete_channel(chat_id_int)
#             logger.info(f"Kanal o'chirildi: chat_id={chat_id_int}")

#     except (ChannelInvalid, PeerIdInvalid):
#         # Kanal allaqachon mavjud emas yoki topilmadi — xatolik deb hisoblamaymiz
#         logger.warning(f"Kanal topilmadi (allaqachon o'chirilgan bo'lishi mumkin): {channel_id}")
#         return

#     except FloodWait as e:
#         if _attempt >= MAX_RETRIES:
#             raise ChannelDeletionError(
#                 f"FloodWait limitiga {MAX_RETRIES} marta duch kelindi, urinish to'xtatildi."
#             )
#         logger.warning(f"FloodWait: {e.value} soniya kutilmoqda (urinish {_attempt}/{MAX_RETRIES})")
#         await asyncio.sleep(e.value)
#         return await delete_channel_by_id(channel_id, _attempt=_attempt + 1)

#     except Exception as e:
#         logger.exception("Kanalni o'chirishda kutilmagan xatolik")
#         raise ChannelDeletionError(str(e)) from e


# """
# Guruh o'chirilganda unga bog'liq Telegram kanalni avtomatik o'chirish xizmati.
# """
# import asyncio
# import logging

# from pyrogram.errors import ChannelInvalid, FloodWait, PeerIdInvalid, RPCError

# from exceptions import ChannelDeletionError
# from userbot_client import userbot

# logger = logging.getLogger(__name__)

# MAX_RETRIES = 3


# async def delete_channel_by_id(channel_id: int, _attempt: int = 1) -> None:
#     """Berilgan chat_id bo'yicha kanalni butunlay o'chiradi."""
#     chat_id_int = int(channel_id)
#     try:
#         async with userbot:
#             try:
#                 await userbot.get_chat(chat_id_int)
#             except Exception as get_err:
#                 logger.warning(f"get_chat ogohlantirishi (davom etamiz): {get_err}")

#             try:
#                 await userbot.delete_channel(chat_id_int)
#                 logger.info(f"Kanal o'chirildi: chat_id={chat_id_int}")
#             except (PeerIdInvalid, ChannelInvalid):
#                 # Agar userbot creator bo'lmasa yoki peer topilmasa, kanalni tark etishga urinib ko'ramiz
#                 logger.warning(f"Kanalni creator sifatida o'chirib bo'lmadi, tark etish bajarilmoqda: {chat_id_int}")
#                 await userbot.leave_chat(chat_id_int)

#     except (ChannelInvalid, PeerIdInvalid):
#         logger.warning(f"Kanal allaqachon mavjud emas yoki kirish imkoni yo'q: {channel_id}")
#         return

#     except FloodWait as e:
#         if _attempt >= MAX_RETRIES:
#             raise ChannelDeletionError(
#                 f"FloodWait limitiga {MAX_RETRIES} marta duch kelindi, urinish to'xtatildi."
#             )
#         logger.warning(f"FloodWait: {e.value} soniya kutilmoqda (urinish {_attempt}/{MAX_RETRIES})")
#         await asyncio.sleep(e.value)
#         return await delete_channel_by_id(channel_id, _attempt=_attempt + 1)

#     except Exception as e:
#         logger.exception("Kanalni o'chirishda kutilmagan xatolik")
#         raise ChannelDeletionError(str(e)) from e
"""
Guruh o'chirilganda unga bog'liq Telegram kanalni avtomatik o'chirish xizmati.
"""
import asyncio
import logging

from pyrogram.errors import ChannelInvalid, FloodWait, PeerIdInvalid, RPCError

from exceptions import ChannelDeletionError
from userbot_client import userbot

logger = logging.getLogger(__name__)

MAX_RETRIES = 3


async def delete_channel_by_id(channel_id: int, _attempt: int = 1) -> None:
    """Berilgan chat_id bo'yicha kanalni butunlay o'chiradi."""
    chat_id_int = int(channel_id)
    try:
        async with userbot:
            me = await userbot.get_me()
            logger.info(f"Userbot sessiyasi: id={me.id}, username={getattr(me, 'username', 'N/A')}")

            try:
                await userbot.get_chat(chat_id_int)
                await userbot.delete_channel(chat_id_int)
                logger.info(f"Kanal o'chirildi: chat_id={chat_id_int}")
            except (PeerIdInvalid, ChannelInvalid, KeyError, ValueError, RPCError) as py_err:
                logger.warning(
                    f"Kanalni o'chirish imkoni bo'lmadi (chat_id={chat_id_int}, sabab: {py_err}). "
                    f"Userbot creator emas yoki keshda mavjud emas. O'tkazib yuborildi."
                )
                return

    except FloodWait as e:
        if _attempt >= MAX_RETRIES:
            raise ChannelDeletionError(
                f"FloodWait limitiga {MAX_RETRIES} marta duch kelindi, urinish to'xtatildi."
            )
        logger.warning(f"FloodWait: {e.value} soniya kutilmoqda (urinish {_attempt}/{MAX_RETRIES})")
        await asyncio.sleep(e.value)
        return await delete_channel_by_id(channel_id, _attempt=_attempt + 1)

    except ChannelDeletionError:
        raise

    except Exception as e:
        logger.exception("Kanalni o'chirishda kutilmagan xatolik")
        raise ChannelDeletionError(str(e)) from e