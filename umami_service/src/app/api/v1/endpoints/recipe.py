"""Обработчики запросов, связанных с рецептами."""


from fastapi import APIRouter, Path

from app.schemas import recipe


router = APIRouter()


@router.get("")
async def get_recipes_by_search_string(
    search_string: str = Path(),
) -> list[recipe.RecipeSimple]:
    """Возвращает список рецептов по строке поиска.

    Args:
        search_string: Строка поиска.

    Returns:
        Список рецептов.
    """


@router.post("/create")
async def create_recipe(
    recipe: recipe.RecipeCreate,
) -> recipe.RecipeCreate:
    """Создает рецепт.

    Args:
        recipe: Объект создаваемого рецепта.

    Returns:
        _description_
    """
    # FIXME
    return recipe
