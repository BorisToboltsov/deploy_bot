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


async def pull_view(telegram_id: int, response: GitCommandError) -> NoReturn:
    if response is None:
        context = "Готово"
    else:
        stderr = response.stderr.split('\n')
        if stderr[1] == "  stderr: 'fatal: Need to specify how to reconcile divergent branches.'":
            context = "Конфликт при слиянии веток!"
        else:
            context = response.stderr
    await EntityMessage.send_message_from_user(telegram_id, context)


async def checkout_view(telegram_id: int) -> NoReturn:
    context = "Введите название ветки"
    await EntityMessage.send_message_from_user(telegram_id, context)


async def set_checkout_view(
    telegram_id: int, response: GitCommandError | None, branch_name: str
) -> NoReturn:
    if response is None:
        context = "Готово"
    else:
        stderr = response.stderr.split('\n')
        if stderr[1] == f"  stderr: 'error: pathspec '{branch_name}' did not match any file(s) known to git'":
            context = "Такой ветки не существует"
        elif stderr[1] == "  stderr: 'error: Your local changes to the following files would be overwritten by checkout:":
            context = f"Нельзя переключить ветку, есть незакомиченные изменения:\n{stderr[2]}\nНужно сделать Reset."
        else:
            context = response.stderr
    await EntityMessage.send_message_from_user(telegram_id, context)


async def reset_view(telegram_id: int, response: GitCommandError | None) -> NoReturn:
    if response is None:
        context = "Готово"
    else:
        context = response.stderr
    await EntityMessage.send_message_from_user(telegram_id, context)


async def status_view(telegram_id: int, response: str) -> NoReturn:
    context = response.replace('<', '"').replace('>', '"')
    await EntityMessage.send_message_from_user(telegram_id, context)
