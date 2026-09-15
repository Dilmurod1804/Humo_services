"""
Channel Service uchun maxsus xatolik klasslari.
"""


class ChannelServiceError(Exception):
    """Umumiy Channel Service xatoligi."""


class ChannelCreationError(ChannelServiceError):
    """Kanal yaratishda yuz bergan xatolik."""


class ChannelDeletionError(ChannelServiceError):
    """Kanalni o'chirishda yuz bergan xatolik."""
