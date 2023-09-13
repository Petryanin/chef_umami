"""Модуль инициализации объектов конфигурации бота."""

from aiogram import Bot, Dispatcher

from app.config import bot_config, init_logging_config


init_logging_config()

bot = Bot(token=bot_config.bot_token.get_secret_value(), parse_mode="HTML")
dp = Dispatcher()
