"""Схемы рецептов."""


from pydantic import BaseModel


class RecipeSimple(BaseModel):
    """Простая схема рецепта."""

    recipe_id: int
    name: str
    description: str
