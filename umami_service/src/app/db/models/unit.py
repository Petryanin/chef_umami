"""Модель единицы измерения ингредиента."""

from sqlalchemy.orm import Mapped, Relationship, mapped_column, relationship

from app.db import const
from app.db.models.base import Base


class Unit(Base):
    """Класс модели единицы измерения ингредиента."""

    __tablename__ = "unit"

    unit_id: Mapped[const.DBTypes.integer] = mapped_column(primary_key=True)
    short_name: Mapped[const.DBTypes.varchar_50]
    full_name: Mapped[const.DBTypes.varchar_255] = mapped_column(unique=True)

    recipe_ingredients: Mapped[Relationship] = relationship(
        "RecipeIngredient", back_populates="unit"
    )
