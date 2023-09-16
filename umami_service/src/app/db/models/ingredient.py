"""Модель ингредиента."""

from sqlalchemy.orm import Mapped, mapped_column

from app.db import const
from app.db.models.base import Base


class IngredientModel(Base):
    """Класс модели ингредиента."""

    __tablename__ = "ingredient"

    ingredient_id: Mapped[const.DBTypes.integer] = mapped_column(primary_key=True)
    name: Mapped[const.DBTypes.varchar_255] = mapped_column(nullable=False)
