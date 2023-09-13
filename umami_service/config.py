"""Модуль конфигурации бота."""

import logging.config
import yaml
from typing import Any

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Класс для хранения настроек приложения.

    Использует Pydantic для валидации и парсинга настроек из файла конфигурации.
    """

    model_config = SettingsConfigDict(
        env_file="umami_service/.env", env_file_encoding="utf-8"
    )


app_config = Settings()


def get_logging_config() -> dict[str, Any]:
    """Инициализирует конфигурацию логгера приложения."""
    with open("logging_config.yaml", "r") as config_file:
        config = yaml.safe_load(config_file)

    logging.config.dictConfig(config)

    return config
