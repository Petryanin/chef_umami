"""Обработчик команды `/start`."""
from aiogram import types
from aiogram.filters.command import Command

from app.config import bot_config
from app.loader import dp
from app.messages import ru


@dp.message(Command("start"))
async def start_command(message: types.Message) -> None:
    """Обработчик команды `/start`.

    Args:
        message: Объект сообщения от пользователя.
    """
    await message.answer(ru.START_MESSAGE.format(bot_config.chef_name))
