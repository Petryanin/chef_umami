"""Обработчики сообщений от пользователя."""

from aiogram import types, F

from tgbot.messages import ru
from tgbot.loader import dp


@dp.message(F.text.regexp("^(?<!//)"))
async def process_unknown_msg(message: types.Message) -> None:
    """Обработчик непонятного сообщения.

    Args:
        message: Объект сообщения от пользователя.
    """
    await message.answer(ru.UNKNOWN_MESSAGE)
