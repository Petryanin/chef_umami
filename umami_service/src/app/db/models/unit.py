"""Модель единицы измерения ингредиента."""

from sqlalchemy.orm import Mapped, mapped_column

from app.db import const
from app.db.models.base import Base


class UnitModel(Base):
    """Класс модели единицы измерения ингредиента."""

    __tablename__ = "unit"

    uint_id: Mapped[const.DBTypes.integer] = mapped_column(primary_key=True)
    short_name: Mapped[const.DBTypes.varchar_50] = mapped_column(nullable=False)
    full_name: Mapped[const.DBTypes.varchar_255] = mapped_column(nullable=False)
