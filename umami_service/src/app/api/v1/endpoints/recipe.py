"""Обработчики запросов, связанных с рецептами."""


from fastapi import APIRouter, Path

from app.schemas.recipe import RecipeSimple


router = APIRouter()


@router.get("")
async def get_recipes_by_search_string(
    search_string: str = Path(),
) -> list[RecipeSimple]:
    """Возвращает список рецептов по строке поиска.

    Args:
        search_string: Строка поиска.

    Returns:
        Список рецептов.
    """
