from typing import NoReturn

from bot.keyboards.markup_keyboard import get_markup_main_menu_keyboard
from bot.keyboards.markup_menu_list import GIT_MENU_FOR_DEVELOPERS
from bot.utils.send_message import EntityMessage


async def git_menu_view(telegram_id: int) -> NoReturn:
    context = "Выберите пункт меню"
    await EntityMessage.send_message_from_user(
        telegram_id, context, get_markup_main_menu_keyboard(GIT_MENU_FOR_DEVELOPERS)
    )