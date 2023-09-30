"""Модуль конфигурации базы данных."""

from sqlalchemy import TextClause
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.sql import text

from app.core.config import app_config
from app.db import const
from app.db import models  # noqa

engine = create_async_engine(const.DATABASE_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(engine)


def load_query_tmpl_from_file(file_name: str) -> TextClause:
    """Загружает шаблон запроса из файла.

    Args:
        file_name: Имя sql-файла

    Returns:
        Шаблон запроса
    """
    with open(f"{app_config.postgres_tmpl_dir}{file_name}") as file:
        return text(file.read())
