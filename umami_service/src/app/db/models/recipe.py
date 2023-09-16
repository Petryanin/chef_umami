"""Модель рецепта."""

from sqlalchemy.orm import Mapped, mapped_column

from app.db import const
from app.db.models.base import Base


class RecipeModel(Base):
    """Класс модели рецепта."""

    __tablename__ = "recipe"

    recipe_id: Mapped[const.DBTypes.integer] = mapped_column(primary_key=True)
    name: Mapped[const.DBTypes.varchar_50] = mapped_column(nullable=False)
    description: Mapped[const.DBTypes.varchar_255] = mapped_column()
    instructions: Mapped[const.DBTypes.text] = mapped_column()
    cooking_time: Mapped[const.DBTypes.smallint] = mapped_column()
    servings: Mapped[const.DBTypes.smallint] = mapped_column()
    difficulty: Mapped[const.DBTypes.smallint] = mapped_column()
    category: Mapped[const.DBTypes.smallint] = mapped_column()
