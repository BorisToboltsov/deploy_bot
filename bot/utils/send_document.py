from typing import NoReturn

from bot.connect import bot


class EntityDocument:
    @staticmethod
    async def send_document(
        telegram_id, photo, caption=None, keyboard=None
    ) -> NoReturn:
        await bot.send_document(
            telegram_id, photo, caption=caption, reply_markup=keyboard
        )
