"""Модель ингредиента."""

from sqlalchemy.orm import Mapped, Relationship, mapped_column, relationship

from app.db import const
from app.db.models.base import Base


class Ingredient(Base):
    """Класс модели ингредиента."""

    __tablename__ = "ingredient"

    ingredient_id: Mapped[const.DBTypes.integer] = mapped_column(primary_key=True)
    name: Mapped[const.DBTypes.varchar_255] = mapped_column(unique=True)

    recipes: Mapped[Relationship] = relationship(
        "Recipe", secondary="recipe_ingredient", back_populates="ingredients"
    )
