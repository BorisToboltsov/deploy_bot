from typing import NoReturn

from bot.keyboards.markup_keyboard import keyboard_remove
from bot.utils.send_message import EntityMessage


async def access_denied(telegram_id: int) -> NoReturn:
    context = f"""Доступ запрещен. Ваш telegram_id: {telegram_id}"""

    await EntityMessage.send_message_from_user(
        telegram_id,
        context,
        keyboard_remove()
    )