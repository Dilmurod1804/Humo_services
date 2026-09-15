"""
Userbot uchun StringSession yaratish — BIR MARTALIK sozlash skripti.

Ishlatilishi:
    python generate_session.py

Jarayon:
  1. my.telegram.org saytidan olingan api_id va api_hash so'raladi
  2. Telefon raqami va Telegramdan kelgan tasdiqlash kodi so'raladi
     (agar 2FA yoqilgan bo'lsa, parol ham so'raladi)
  3. Muvaffaqiyatli avtorizatsiyadan so'ng StringSession konsolga chiqariladi

Hosil bo'lgan StringSession qiymatini channel_service/.env faylidagi
SESSION_STRING o'zgaruvchisiga joylashtiring.

⚠️ DIQQAT: Bu sessiya to'liq Telegram akkauntga kirish huquqini beradi.
Uni hech qachon git repozitoriyga qo'shmang yoki uchinchi shaxslarga bermang.
"""
from pyrogram import Client


def main() -> None:
    print("=== Humo Kids — Userbot sessiyasini yaratish ===\n")
    api_id = int(input("api_id (my.telegram.org dan): ").strip())
    api_hash = input("api_hash (my.telegram.org dan): ").strip()

    with Client(
        name="session_generator",
        api_id=api_id,
        api_hash=api_hash,
        in_memory=True,
    ) as app:
        session_string = app.export_session_string()

    print("\n✅ Sessiya muvaffaqiyatli yaratildi!\n")
    print("Quyidagi qiymatni channel_service/.env faylidagi SESSION_STRING ga joylashtiring:\n")
    print(session_string)
    print()


if __name__ == "__main__":
    main()
