"""Модуль запуска бота."""

import asyncio
import logging


from tgbot.loader import dp, bot


# def register_all_middlewares(dispatcher: Dispatcher) -> None:
#     logging.info("Registering middlewares")
#     dispatcher.setup_middleware(ThrottlingMiddleware())


def register_all_handlers() -> None:
    """Регистрирует все хэндлеры бота."""
    logging.info("Registering handlers")

    from tgbot import handlers  # noqa: F401


# async def register_all_commands(dispatcher: Dispatcher) -> None:
#     logging.info("Registering commands")
#     await set_default_commands(dispatcher.bot)


# async def on_startup(dispatcher: Dispatcher, webhook_url: str = None) -> None:
#     register_all_middlewares(dispatcher)
#     register_all_handlers(dispatcher)
#     await register_all_commands(dispatcher)

#     # Get current webhook status
#     webhook = await dispatcher.bot.get_webhook_info()

#     if webhook_url:
#         await dispatcher.bot.set_webhook(webhook_url)
#         logging.info("Webhook was set")
#     elif webhook.url:
#         await dispatcher.bot.delete_webhook()
#         logging.info("Webhook was deleted")

#     await on_startup_notify(dispatcher)

#     logging.info("Bot started")


# async def on_shutdown(dispatcher: Dispatcher) -> None:
#     await dispatcher.storage.close()
#     await dispatcher.storage.wait_closed()
#     logging.info("Bot shutdown")


async def main() -> None:
    """Точка входа."""
    logging.info("Initializing bot")

    register_all_handlers()

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
