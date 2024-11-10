from typing import NoReturn

from bot.connect import bot


class EntityPhoto:
    @staticmethod
    async def send_photo(telegram_id, photo, caption=None, keyboard=None) -> NoReturn:
        await bot.send_photo(telegram_id, photo, caption=caption, reply_markup=keyboard)
