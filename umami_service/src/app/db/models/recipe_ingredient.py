"""Связь рецепты-ингредиенты."""

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db import const
from app.db.models.base import Base


class RecipeIngredientModel(Base):
    """Класс связи рецепты-ингредиенты."""

    __tablename__ = "recipe_ingredient"

    recipe_ingredient_id: Mapped[const.DBTypes.integer] = mapped_column(
        primary_key=True
    )
    recipe_id: Mapped[const.DBTypes.integer] = mapped_column(
        ForeignKey("recipe.recipe_id", ondelete="CASCADE")
    )
    ingredient_id: Mapped[const.DBTypes.integer] = mapped_column(
        ForeignKey("ingredient.ingredient_id", ondelete="CASCADE")
    )
    unit_id: Mapped[const.DBTypes.integer] = mapped_column(ForeignKey("unit.unit_id"))
    amount: Mapped[const.DBTypes.numeric | None]
    sort: Mapped[const.DBTypes.smallint | None]
