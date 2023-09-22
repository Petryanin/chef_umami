"""Обработчики запросов, связанных с рецептами."""


from fastapi import APIRouter, Path

from app.schemas import recipe


router = APIRouter()


@router.get("")
async def get_recipes_list(
    search_string: str = Path(),
) -> list[recipe.RecipeSimple]:
    """Возвращает список рецептов.

    Args:
        search_string: Строка поиска.

    Returns:
        Список рецептов.
    """


@router.post("")
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
