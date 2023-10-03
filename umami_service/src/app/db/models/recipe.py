"""Модель рецепта."""

from __future__ import annotations

from typing import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column, relationship, selectinload

from app import schemas
from app.db import config as db_config
from app.db import const
from app.db import models


class Recipe(models.Base):
    """Класс модели рецепта."""

    __tablename__ = "recipe"

    recipe_id: Mapped[const.DBTypes.integer] = mapped_column(primary_key=True)
    name: Mapped[const.DBTypes.varchar_50] = mapped_column(unique=True)
    description: Mapped[const.DBTypes.varchar_255 | None]
    instructions: Mapped[const.DBTypes.text | None]
    cooking_time: Mapped[const.DBTypes.smallint | None]
    servings: Mapped[const.DBTypes.smallint | None]
    difficulty: Mapped[const.DBTypes.smallint | None]
    category: Mapped[const.DBTypes.smallint | None]

    ingredients: Mapped[list[models.RecipeIngredient]] = relationship(
        "RecipeIngredient",
        back_populates="recipe",
        order_by=models.RecipeIngredient.sort,
    )

    @staticmethod
    async def create(
        db_session: AsyncSession,
        recipe: schemas.RecipeCreate,
    ) -> int | None:
        """Создает рецепт.

        Args:
            db_session: Объект сессии БД.
            recipe: Объект создаваемого рецепта.

        Returns:
            ID созданного рецепта.
        """
        query = db_config.load_query_tmpl_from_file("create_recipe.sql")
        params = {
            "recipe_name": recipe.name,
            "recipe_description": recipe.description,
            "recipe_instructions": recipe.instructions,
            "cooking_time": recipe.cooking_time,
            "servings": recipe.servings,
            "difficulty": recipe.difficulty,
            "category": recipe.category,
            "ingredient_names": [ingredient.name for ingredient in recipe.ingredients],
            "unit_short_names": [
                ingredient.unit.short_name for ingredient in recipe.ingredients
            ],
            "unit_full_names": [
                ingredient.unit.full_name for ingredient in recipe.ingredients
            ],
            "amounts": [ingredient.amount for ingredient in recipe.ingredients],
            "sorts": [ingredient.sort for ingredient in recipe.ingredients],
        }
        result = await db_session.execute(query, params)
        await db_session.commit()

        return result.scalars().first()

    @staticmethod
    async def get_all(
        db_session: AsyncSession,
        *,
        with_ingredients: bool = True,
        with_units: bool = True,
    ) -> Sequence[Recipe]:
        """Возвращает список всех рецептов.

        Args:
            db_session: Объект сессии БД.
            with_ingredients: Флаг: с ингредиентами.
            with_units: Флаг: с единицами измерения.

        Returns:
            Список рецептов.
        """
        opts = []

        if with_ingredients:
            opt = selectinload(Recipe.ingredients)
            if with_units:
                opt = opt.joinedload(models.RecipeIngredient.unit)

            opts.append(opt)

        stmt = select(Recipe).options(*opts)

        result = await db_session.execute(stmt)

        return result.unique().scalars().all()
