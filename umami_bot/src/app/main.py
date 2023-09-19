"""Модуль запуска бота."""

import asyncio

from app.loader import bot, dp, init_all


async def main() -> None:
    """Точка входа."""
    init_all()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
