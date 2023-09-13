"""Основной модуль."""

import logging

import uvicorn
from fastapi import FastAPI

from app import config
from app.middlewares.logging import LoggingMiddleware


app = FastAPI(
    title="Umami Chef",
    description="Your cooking companion!",
    version="0.1.0",
)

app.add_middleware(LoggingMiddleware)


@app.get("/")
async def index() -> dict:
    """Обработчик начальной страницы."""
    return {"message": "Hello, this is the index page!"}


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        log_config=config.get_logging_config( ),
        log_level=logging.DEBUG,
        reload=True,
    )
