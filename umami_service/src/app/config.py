"""Модуль конфигурации бота."""

import logging.config
import yaml
from typing import Any

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Класс для хранения настроек приложения.

    Использует Pydantic для валидации и парсинга настроек из файла конфигурации.
    """

    logging_config_path: str

    model_config = SettingsConfigDict(
        env_file="../.env", env_file_encoding="utf-8"
    )


app_config = Settings()


def get_logging_config() -> dict[str, Any]:
    """Инициализирует конфигурацию логгера приложения."""
    with open(app_config.logging_config_path, "r") as config_file:
        config = yaml.safe_load(config_file)

    logging.config.dictConfig(config)

    return config
