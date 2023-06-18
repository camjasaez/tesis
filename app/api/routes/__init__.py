# Router principal
from fastapi import APIRouter
from .status_route import router as status_router
from .cars_route import router as cars_router

api_router = APIRouter()

api_router.include_router(status_router, prefix="/status", tags=["status"])
api_router.include_router(cars_router, prefix="/cars", tags=["cars"])
