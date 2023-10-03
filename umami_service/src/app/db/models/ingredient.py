"""Модель ингредиента."""
from __future__ import annotations

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db import const
from app.db import models


class Ingredient(models.Base):
    """Класс модели ингредиента."""

    __tablename__ = "ingredient"

    ingredient_id: Mapped[const.DBTypes.integer] = mapped_column(primary_key=True)
    name: Mapped[const.DBTypes.varchar_255] = mapped_column(unique=True)

    recipes: Mapped[list[models.Recipe]] = relationship(
        "RecipeIngredient",
        back_populates="ingredient",
    )
