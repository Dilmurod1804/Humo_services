"""
FastAPI so'rov/javob (request/response) sxemalari.
"""
from typing import Optional

from pydantic import BaseModel, Field


class CreateChannelRequest(BaseModel):
    title: str = Field(..., min_length=1, max_length=128)
    description: Optional[str] = None


class CreateChannelResponse(BaseModel):
    channel_id: int
    invite_link: str
    status: str = "success"


class DeleteChannelRequest(BaseModel):
    channel_id: int


class DeleteChannelResponse(BaseModel):
    status: str = "success"


class ErrorResponse(BaseModel):
    status: str = "error"
    detail: str
