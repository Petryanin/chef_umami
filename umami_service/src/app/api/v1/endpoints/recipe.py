"""Обработчики запросов, связанных с рецептами."""

from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app import schemas
from app.core.dependencies import get_db_session
from app.db.models.recipe import Recipe


router = APIRouter()


@router.get("")
async def get_recipes_list(
    db_session: AsyncSession = Depends(get_db_session),
    with_ingredients: bool = True,
    with_units: bool = True,
):
    """Возвращает список рецептов.

    Args:
        db_session: Объект сессии БД.
        with_ingredients: Флаг: с ингредиентами.
        with_units: Флаг: с единицами измерения.

    Returns:
        Список рецептов.
    """
    return await Recipe.get_all(
        db_session, with_ingredients=with_ingredients, with_units=with_units
    )


@router.post("")
async def create_recipe(
    recipe: schemas.RecipeCreate, db_session: AsyncSession = Depends(get_db_session)
) -> schemas.RecipeCreateSuccess:
    """Создает рецепт.

    Args:
        recipe: Объект создаваемого рецепта.
        db_session: Объект сессии БД.

    Returns:
        None
    """
    recipe_id = await Recipe.create(db_session, recipe)

    if not recipe_id:
        raise HTTPException(
            HTTPStatus.INTERNAL_SERVER_ERROR, detail="Error creating recipe"
        )

    return schemas.RecipeCreateSuccess(
        recipe_id=recipe_id, message="Recipe successfully created"
    )
