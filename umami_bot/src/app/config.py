"""Модуль конфигурации бота."""

import logging.config
import yaml

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Класс для хранения настроек приложения.

    Использует Pydantic для валидации и парсинга настроек из файла конфигурации.
    """

    bot_token: SecretStr
    chef_name: str
    logging_config_path: str

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8"
    )


bot_config = Settings()


def init_logging_config() -> None:
    """Инициализирует конфигурацию логгера приложения."""
    with open(bot_config.logging_config_path, "r") as config_file:
        config = yaml.safe_load(config_file)

    logging.config.dictConfig(config)
