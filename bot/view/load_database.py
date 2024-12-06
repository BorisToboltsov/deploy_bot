from typing import NoReturn

from bot.utils.send_message import EntityMessage


async def load_database_start_view(telegram_id: int) -> NoReturn:
    context = "Запуск загрузки базы данных, время выполнения около 5 минут."
    await EntityMessage.send_message_from_user(
        telegram_id, context
    )


async def load_database_complete_view(telegram_id: int) -> NoReturn:
    context = "Загрузка базы данных успешно завершена."
    await EntityMessage.send_message_from_user(
        telegram_id, context
    )

async def load_database_file_not_found_view(telegram_id: int) -> NoReturn:
    context = "Файл бэкапа не найден."
    await EntityMessage.send_message_from_user(
        telegram_id, context
    )


async def load_database_active_view(telegram_id: int) -> NoReturn:
    context = "База данных загружается, подождите."
    await EntityMessage.send_message_from_user(
        telegram_id, context
    )


async def load_database_error_view(telegram_id: int) -> NoReturn:
    context = "Ошибка загрузки"
    await EntityMessage.send_message_from_user(
        telegram_id, context
    )
