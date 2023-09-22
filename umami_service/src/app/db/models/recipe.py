"""Модель рецепта."""

from sqlalchemy.orm import Mapped, mapped_column, Relationship, relationship

from app.db import const
from app.db.models.base import Base
from app.db.models.ingredient import IngredientModel


class RecipeModel(Base):
    """Класс модели рецепта."""

    __tablename__ = "recipe"

    recipe_id: Mapped[const.DBTypes.integer] = mapped_column(primary_key=True)
    name: Mapped[const.DBTypes.varchar_50]
    description: Mapped[const.DBTypes.varchar_255 | None]
    instructions: Mapped[const.DBTypes.text | None]
    cooking_time: Mapped[const.DBTypes.smallint | None]
    servings: Mapped[const.DBTypes.smallint | None]
    difficulty: Mapped[const.DBTypes.smallint | None]
    category: Mapped[const.DBTypes.smallint | None]

    ingredients: Mapped[Relationship[IngredientModel]] = relationship(
        "RecipeIngredient", back_populates="recipe"
    )
