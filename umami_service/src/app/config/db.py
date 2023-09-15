"""Модуль конфигурации базы данных."""


from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.config.common import app_config


DATABASE_URL = URL.create(
    drivername="postgresql+asyncpg",
    username=app_config.db_user,
    password=app_config.db_password,
    host=app_config.db_host,
    port=app_config.db_port,
    database=app_config.db_name,
)


POSTGRES_INDEXES_NAMING_CONVENTION = {
    "ix": "%(column_0_label)s_idx",
    "uq": "%(table_name)s_%(column_0_name)s_key",
    "ck": "%(table_name)s_%(constraint_name)s_check",
    "fk": "%(table_name)s_%(column_0_name)s_fkey",
    "pk": "%(table_name)s_pkey",
}


engine = create_async_engine(DATABASE_URL)
AsyncSessionLocal = async_sessionmaker(engine)


class Base(DeclarativeBase):
    """Базовый класс, используемый для декларативных определений моделей."""

    metadata = MetaData(naming_convention=POSTGRES_INDEXES_NAMING_CONVENTION)

metadata = Base.metadata
