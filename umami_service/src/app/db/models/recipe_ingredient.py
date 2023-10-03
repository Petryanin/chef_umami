"""Связь рецепты-ингредиенты."""

from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import const
from app.db import models


class RecipeIngredient(models.Base):
    """Класс модели ингредиента в рецепте."""

    __tablename__ = "recipe_ingredient"

    recipe_ingredient_id: Mapped[const.DBTypes.integer] = mapped_column(
        primary_key=True
    )
    recipe_id: Mapped[const.DBTypes.integer] = mapped_column(
        ForeignKey(
            "recipe.recipe_id",
            ondelete="CASCADE",
        ),
    )
    ingredient_id: Mapped[const.DBTypes.integer] = mapped_column(
        ForeignKey("ingredient.ingredient_id"),
    )
    unit_id: Mapped[const.DBTypes.integer] = mapped_column(ForeignKey("unit.unit_id"))
    amount: Mapped[const.DBTypes.numeric | None]
    sort: Mapped[const.DBTypes.smallint | None]

    unit: Mapped[models.Unit] = relationship(
        "Unit",
        back_populates="recipe_ingredients",
    )
    recipe: Mapped[models.Recipe] = relationship(
        "Recipe",
        back_populates="ingredients",
    )
    ingredient: Mapped[models.Ingredient] = relationship(
        "Ingredient",
        back_populates="recipes",
        lazy="joined",
    )
