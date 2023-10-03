"""Схемы, связанные с рецептами."""
import enum
import re

from pydantic import BaseModel
from pydantic import field_validator

from app.schemas.ingredient import RecipeIngredient


class RecipeDifficulty(enum.IntEnum):
    """Перечисление сложностей приготовления."""

    BABY = enum.auto()
    EASY = enum.auto()
    MEDIUM = enum.auto()
    HARD = enum.auto()
    EXPERT = enum.auto()


class RecipeSimple(BaseModel):
    """Простая схема рецепта."""

    recipe_id: int
    name: str
    description: str


class RecipeCreate(BaseModel):
    """Cхема создания рецепта."""

    name: str
    description: str | None
    instructions: str | None
    cooking_time: int | None
    servings: int | None
    difficulty: RecipeDifficulty | None
    category: int | None
    ingredients: list[RecipeIngredient]

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        """Валидирует название рецепта.

        Args:
            value: Значение валидируемого параметра.

        Raises:
            ValueError: Если название не соответствует требованиям.

        Returns:
            Распарсенный параметр.
        """
        value = value.strip()
        pattern = r"^[A-Za-zА-Яа-яÉéÈèÀàÙùÇçÜüÖöÂâÊêÎîÔôÎîÛûËëÏï\s\-_]{1,50}$"

        if not re.match(pattern, value):
            raise ValueError("Invalid recipe name")

        return value

    @field_validator("description")
    @classmethod
    def validate_description(cls, value: str) -> str:
        """Валидирует название рецепта.

        Args:
            value: Значение валидируемого параметра.

        Raises:
            ValueError: Если название не соответствует требованиям.

        Returns:
            Распарсенный параметр.
        """
        value = value.strip()
        pattern = r"^[A-Za-zА-Яа-яÉéÈèÀàÙùÇçÜüÖöÂâÊêÎîÔôÎîÛûËëÏï\s\-_]{1,255}$"

        if not re.match(pattern, value):
            raise ValueError("Invalid description")

        return value


class RecipeCreateSuccess(BaseModel):
    """Схема успешного создания рецепта."""

    recipe_id: int
    message: str
