"""
MTProto userbot klienti (Pyrogram).

Bu klient oldindan avtorizatsiya qilingan StringSession orqali ishlaydi
(generate_session.py skripti bilan bir marta yaratiladi). Qayta login
talab qilinmaydi.
"""
from pyrogram import Client

from config import settings

userbot = Client(
    name="humo_kids_userbot",
    api_id=settings.api_id,
    api_hash=settings.api_hash,
    session_string=settings.session_string,
    in_memory=True,
)
