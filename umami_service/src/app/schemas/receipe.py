"""Схемы рецептов."""


from pydantic import BaseModel


class ReceipeSimple(BaseModel):
    """Простая схема рецепта."""

    receipe_id: int
    name: str
    description: str
