from typing import NoReturn

from bot.utils.send_message import EntityMessage


async def work_packages_view(telegram_id: int, message: str) -> NoReturn:
    context = message
    await EntityMessage.send_message_from_user(telegram_id, context)
