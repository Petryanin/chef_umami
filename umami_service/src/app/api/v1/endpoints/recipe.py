"""Обработчики запросов, связанных с рецептами."""
from http import HTTPStatus

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app import schemas
from app.core.dependencies import get_db_session
from app.db.models.recipe import Recipe


router = APIRouter()


@router.get(
    "",
    response_model_exclude_defaults=True,
)
async def get_recipes_list(
    db_session: AsyncSession = Depends(get_db_session),
    with_ingredients: bool = True,
) -> list[schemas.RecipeFull]:
    """Возвращает список рецептов.

    Args:
        db_session: Объект сессии БД.
        with_ingredients: Флаг: с ингредиентами.

    Returns:
        Список рецептов.
    """
    recipes = await Recipe.get_all(
        db_session,
        with_ingredients=with_ingredients,
    )
    return [schemas.RecipeFull.model_validate(recipe) for recipe in recipes]


@router.post("", status_code=HTTPStatus.CREATED)
async def create_recipe(
    recipe: schemas.RecipeCreate,
    db_session: AsyncSession = Depends(get_db_session),
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
