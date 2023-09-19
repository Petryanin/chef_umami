"""Основной модуль."""

import logging

import uvicorn
from fastapi import FastAPI

from app import config, loader


app = FastAPI(
    title="Umami Chef",
    description="Your cooking companion!",
    version="0.1.0",
)


@app.get("/")
async def index() -> dict:
    """Обработчик начальной страницы."""
    return {"message": "Hello, this is the index page!"}


if __name__ == "__main__":
    loader.init_all(app)
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8080,
        log_config=config.logging_config,
        log_level=logging.DEBUG,
        reload=True,
    )
