"""Обработчики запросов, связанных с рецептами."""


from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.ext.asyncio import AsyncSession

from app import schemas
from app.core.dependencies import get_db_session
from app.db.models.recipe import Recipe


router = APIRouter()


@router.get("")
async def get_recipes_list(
    search_string: str = Path(),
) -> list[schemas.RecipeSimple]:
    """Возвращает список рецептов.

    Args:
        search_string: Строка поиска.

    Returns:
        Список рецептов.
    """


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
