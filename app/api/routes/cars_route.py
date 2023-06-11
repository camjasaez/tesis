from fastapi import APIRouter
from api.controllers.cars_controller import get_all_cars
from utils.responses import success_response, error_response

router = APIRouter()


@router.get("/", response_description="Get all cars")
async def get_all():
    cars = await get_all_cars()
    if cars:
        return success_response(data=cars)
    if cars.__len__() == 0:
        return error_response(status=204, message="No cars")
    return error_response(status=500, message="Something went wrong")
