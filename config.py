"""
Channel Service (backend) konfiguratsiyasi.
Bu xizmat MTProto (Pyrogram) orqali Telegram kanallarini avtomatik
yaratish/o'chirish bilan shug'ullanadi.
"""
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):
    # my.telegram.org saytidan olingan hisob ma'lumotlari
    api_id: int
    api_hash: str

    # generate_session.py skripti orqali bir marta yaratiladigan sessiya satri
    session_string: str

    # Asosiy Humo Kids botining username'i (masalan: "@HumoKidsBot")
    # Kanal yaratilgandan so'ng shu bot admin sifatida qo'shiladi
    bot_username: str

    # Bot bilan ichki aloqani himoyalovchi token
    # (humo_kids_bot/.env dagi INTERNAL_API_TOKEN bilan bir xil bo'lishi shart)
    internal_api_token: str

    host: str = "0.0.0.0"
    port: int = 8001

    model_config = SettingsConfigDict(
        env_file=str(BASE_DIR / ".env"),
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()
