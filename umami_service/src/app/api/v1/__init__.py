"""V1."""

from fastapi import APIRouter

from app.api.v1.endpoints import (
    recipe as api_recipe,
)


api_router = APIRouter()

api_router.include_router(api_recipe.router, prefix="/recipes", tags=["recipes"])
