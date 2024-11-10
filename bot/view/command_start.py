from typing import NoReturn

from bot.keyboards.inline_keyboard import get_builder_inline_keyboard
from bot.utils.send_message import EntityMessage


async def change_project(telegram_id: int, button_menu: list) -> NoReturn:
    context = f"""Выберите проект"""
    await EntityMessage.send_message_from_user(telegram_id, context, await get_builder_inline_keyboard(button_menu, 2))