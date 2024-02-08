from aiogram import types
from aiogram.filters import Filter

from data.config import ADMIN_IDS


class IsAdmin(Filter):
    async def __call__(self, message: types.Message):
        for admin_id in ADMIN_IDS:
            if message.from_user.id == admin_id:
                return True
        return False
