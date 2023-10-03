"""Модель единицы измерения ингредиента."""
from __future__ import annotations

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Relationship
from sqlalchemy.orm import relationship

from app.db import const
from app.db import models


class Unit(models.Base):
    """Класс модели единицы измерения ингредиента."""

    __tablename__ = "unit"

    unit_id: Mapped[const.DBTypes.integer] = mapped_column(primary_key=True)
    short_name: Mapped[const.DBTypes.varchar_50]
    full_name: Mapped[const.DBTypes.varchar_255] = mapped_column(unique=True)

    recipe_ingredients: Mapped[Relationship] = relationship(
        "RecipeIngredient", back_populates="unit"
    )
