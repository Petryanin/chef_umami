"""Схемы, связанные с ингредиентами."""


from pydantic import BaseModel


class Ingredient(BaseModel):
    """Cхема ингредиента."""

    name: str
