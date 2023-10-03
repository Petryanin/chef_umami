"""Схемы, связанные с ингредиентами."""
import decimal

from pydantic import BaseModel

from app.schemas.unit import UnitCreate


class RecipeIngredient(BaseModel):
    """Cхема ингредиента в рецепте."""

    name: str
    amount: decimal.Decimal | None
    sort: int | None
    unit: UnitCreate
