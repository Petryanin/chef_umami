"""Обработчики запросов, связанных с рецептами."""


from fastapi import APIRouter, Path

from app.schemas.receipe import ReceipeSimple


router = APIRouter()


@router.get("")
async def get_receipes_by_search_string(search_string: str = Path()) -> list[ReceipeSimple]:
    """Возвращает список рецептов по строке поиска.

    Args:
        search_string: Строка поиска.

    Returns:
        Список рецептов.
    """

