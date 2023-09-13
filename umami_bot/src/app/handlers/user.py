"""Обработчики сообщений от пользователя."""

from aiogram import types

from app.messages import ru
from app.loader import dp


@dp.message()
async def process_unknown_msg(message: types.Message) -> None:
    """Обработчик непонятного сообщения.

    Args:
        message: Объект сообщения от пользователя.
    """
    await message.answer(ru.UNKNOWN_MESSAGE)
