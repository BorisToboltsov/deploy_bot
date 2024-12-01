from typing import NoReturn

from bot.utils.send_message import EntityMessage


async def load_database_start_view(telegram_id: int) -> NoReturn:
    context = "Запуск загрузки базы данных"
    await EntityMessage.send_message_from_user(
        telegram_id, context
    )


async def load_database_complete_view(telegram_id: int) -> NoReturn:
    context = "Загрузка базы данных завершена"
    await EntityMessage.send_message_from_user(
        telegram_id, context
    )


async def load_database_error_view(telegram_id: int) -> NoReturn:
    context = "Ошибка загрузки"
    await EntityMessage.send_message_from_user(
        telegram_id, context
    )
