from typing import NoReturn

from git.exc import GitCommandError

from bot.keyboards.markup_keyboard import get_markup_main_menu_keyboard
from bot.keyboards.markup_menu_list import MAIN_MENU_FOR_DEVELOPERS
from bot.utils.send_message import EntityMessage


async def project_settings_view(telegram_id: int) -> NoReturn:
    context = "Выберите, что нужно сделать."
    await EntityMessage.send_message_from_user(
        telegram_id, context, get_markup_main_menu_keyboard(MAIN_MENU_FOR_DEVELOPERS)
    )


async def pull_view(telegram_id: int) -> NoReturn:
    context = "Готово"
    await EntityMessage.send_message_from_user(telegram_id, context)


async def checkout_view(telegram_id: int) -> NoReturn:
    context = "Введите название ветки"
    await EntityMessage.send_message_from_user(telegram_id, context)


async def set_checkout_view(
    telegram_id: int, response: GitCommandError | None
) -> NoReturn:
    if response is None:
        context = "Готово"
    else:
        context = response.stderr
    await EntityMessage.send_message_from_user(telegram_id, context)


async def reset_view(telegram_id: int) -> NoReturn:
    context = "Готово"
    await EntityMessage.send_message_from_user(telegram_id, context)
