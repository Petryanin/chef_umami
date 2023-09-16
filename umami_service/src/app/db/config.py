"""Модуль конфигурации базы данных."""

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.db import const
from app.db.models.base import Base


engine = create_async_engine(const.DATABASE_URL)
AsyncSessionLocal = async_sessionmaker(engine)
metadata = Base.metadata
