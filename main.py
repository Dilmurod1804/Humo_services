"""
Channel Service — FastAPI backend.

Bu xizmat faqat ichki tarmoqda (Docker internal network) ishlashi kerak,
tashqi internetga ochilmasligi lozim. Asosiy Humo Kids bot shu servisga
HTTP orqali murojaat qilib, Telegram kanallarini yaratadi/o'chiradi.

Ishga tushirish (lokal test uchun):
    uvicorn main:app --host 0.0.0.0 --port 8001
"""
import logging

from fastapi import FastAPI, Header, HTTPException, status

from config import settings
from exceptions import ChannelServiceError
from schemas import (
    CreateChannelRequest,
    CreateChannelResponse,
    DeleteChannelRequest,
    DeleteChannelResponse,
)
from services.create_channel import create_channel_for_group
from services.delete_channel import delete_channel_by_id

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Humo Kids — Channel Service",
    description="Telegram kanallarini MTProto orqali avtomatik yaratish/o'chirish xizmati.",
    version="1.0.0",
)


def verify_internal_token(x_internal_token: str = Header(...)) -> None:
    """Faqat asosiy bot (to'g'ri token bilan) so'rov yubora olishini ta'minlaydi."""
    if x_internal_token != settings.internal_api_token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Ruxsat yo'q: ichki token noto'g'ri.",
        )


@app.post("/channels/create", response_model=CreateChannelResponse)
async def create_channel(
    req: CreateChannelRequest,
    x_internal_token: str = Header(...),
) -> CreateChannelResponse:
    verify_internal_token(x_internal_token)
    logger.info(f"Kanal yaratish so'rovi qabul qilindi: {req.title}")

    try:
        result = await create_channel_for_group(req.title, req.description)
    except ChannelServiceError as e:
        logger.error(f"Kanal yaratib bo'lmadi: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    return CreateChannelResponse(
        channel_id=result["channel_id"],
        invite_link=result["invite_link"],
    )


@app.post("/channels/delete", response_model=DeleteChannelResponse)
async def delete_channel(
    req: DeleteChannelRequest,
    x_internal_token: str = Header(...),
) -> DeleteChannelResponse:
    verify_internal_token(x_internal_token)
    logger.info(f"Kanal o'chirish so'rovi qabul qilindi: {req.channel_id}")

    try:
        await delete_channel_by_id(req.channel_id)
    except ChannelServiceError as e:
        logger.error(f"Kanalni o'chirib bo'lmadi: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    return DeleteChannelResponse()


@app.get("/health")
async def health_check() -> dict:
    """Konteyner/health-check tizimlari uchun oddiy tekshiruv endpointi."""
    return {"status": "ok", "service": "channel_service"}
