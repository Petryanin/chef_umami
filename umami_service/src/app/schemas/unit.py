"""Схемы, связанные с единицами измерения."""
from pydantic import BaseModel
from pydantic import ConfigDict


class UnitBase(BaseModel):
    """Базовая схема ЕИ."""

    short_name: str
    full_name: str


class UnitFull(UnitBase):
    """Полная схема ЕИ."""

    model_config = ConfigDict(from_attributes=True)

    unit_id: int


class UnitCreate(UnitBase):
    """Схема создания ЕИ."""
