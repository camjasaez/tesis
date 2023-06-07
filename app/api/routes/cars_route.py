from fastapi import APIRouter
from api.controllers.cars_controller import get_all_cars

router = APIRouter()


@router.get("/cars", response_description="Get all cars")
async def get_all():
    cars = await get_all_cars()
    return {"data": cars, "error": False, "message": "Cars retrieved successfully"}
