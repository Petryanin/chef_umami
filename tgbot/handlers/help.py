"""Обработчик команды `/help`."""

from aiogram import types
from aiogram.filters.command import Command

from tgbot.config import bot_config
from tgbot.messages import ru
from tgbot.loader import dp


@dp.message(Command("help"))
async def help_command(message: types.Message) -> None:
    """Обработчик команды `/help`.

    Args:
        message: Объект сообщения от пользователя.
    """
    await message.answer(ru.HELP_MESSAGE.format(bot_config.chef_name))
