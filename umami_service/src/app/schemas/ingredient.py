"""Схемы, связанные с ингредиентами."""
import decimal

from pydantic import BaseModel
from pydantic import ConfigDict

from app.schemas.unit import UnitCreate
from app.schemas.unit import UnitFull


class IngredientBase(BaseModel):
    """Базовая схема ингредиента."""

    name: str


class IngredientFull(IngredientBase):
    """Полная схема ингредиента."""

    model_config = ConfigDict(from_attributes=True)

    ingredient_id: int


class RecipeIngredientBase(BaseModel):
    """Cхема ингредиента в рецепте."""

    amount: decimal.Decimal | None
    sort: int | None


class RecipeIngredientFull(RecipeIngredientBase):
    """Полная схема ингредиента в рецепте."""

    model_config = ConfigDict(from_attributes=True)

    recipe_ingredient_id: int
    recipe_id: int
    ingredient_id: int
    unit_id: int
    ingredient: IngredientFull | None = None
    unit: UnitFull | None = None


class RecipeIngredientCreate(RecipeIngredientBase):
    """Cхема создания ингредиента в рецепте."""

    unit: UnitCreate
