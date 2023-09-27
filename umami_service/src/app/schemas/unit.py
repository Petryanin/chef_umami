"""Схемы, связанные с единицами измерения."""

from pydantic import BaseModel


class UnitCreate(BaseModel):
    """Схема создания ЕИ."""

    short_name: str
    full_name: str | None
