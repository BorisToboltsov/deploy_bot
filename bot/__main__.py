import asyncio
from typing import NoReturn

from bot.connect import bot, dp
from bot.handlers.commands import router_commands
from bot.middlewares.auth import Auth


async def main() -> NoReturn:

    # Router register
    dp.include_router(router_commands)

    dp.update.middleware(Auth())

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
