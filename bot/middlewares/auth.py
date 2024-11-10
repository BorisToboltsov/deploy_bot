import json
import os
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Update

from bot.view.auth import access_denied


class Auth(BaseMiddleware):
    def __init__(self) -> None:
        super().__init__()

    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any],
    ) -> Any:

        user = data.get("event_from_user")
        telegram_id = user.id
        first_name = user.first_name
        last_name = user.last_name
        username = user.username

        TELEGRAM_IDS = json.loads(os.getenv("TELEGRAM_IDS"))

        if str(telegram_id) not in TELEGRAM_IDS:
            await access_denied(telegram_id)
        else:
            # data["session"] = data
            return await handler(event, data)
