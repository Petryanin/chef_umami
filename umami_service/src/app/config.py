"""Модуль конфигурации сервиса."""

import logging.config
import yaml
from typing import Any

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Класс для хранения настроек приложения.

    Использует Pydantic для валидации и парсинга настроек из файла конфигурации.
    """

    # logging
    logging_config_path: str

    # database
    postgres_user: str
    postgres_password: str
    postgres_name: str
    postgres_port: int
    postgres_host: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


app_config = Settings()


def get_logging_config() -> dict[str, Any]:
    """Инициализирует конфигурацию логгера приложения."""
    with open(app_config.logging_config_path, "r") as config_file:
        config = yaml.safe_load(config_file)

    logging.config.dictConfig(config)

    return config
