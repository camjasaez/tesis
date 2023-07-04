from typing import Annotated, Union
from fastapi import APIRouter, Body
from api.controllers.cars_controller import (
    get_all_cars,
    get_car_by_id,
    get_cars_by_license_plate,
    create_car,
)
from utils.responses import success_response, error_response
from models.cars_model import Car

# /cars
router = APIRouter()


@router.get("/", response_description="Get all cars")
async def get_all():
    cars = await get_all_cars()
    if cars:
        return success_response(data=cars)
    if cars.__len__() == 0:
        return error_response(status=204, message="No cars")
    return error_response(status=500, message="Something went wrong")


@router.get("/{id}", response_description="Get car by id")
async def get_by_id(id: str):
    car = await get_car_by_id(id)
    if car:
        return success_response(data=car)
    return error_response(status=500, message="Something went wrong")


@router.get(
    "/license_plate/{license_plate}", response_description="Get car by license plate"
)
async def get_by_license_plate(license_plate: str):
    car = await get_cars_by_license_plate(license_plate)
    if car:
        return success_response(data=car)
    if car.__len__() == 0:
        return error_response(status=204, message="No cars")
    return error_response(status=500, message="Something went wrong")


@router.post("/", response_description="Create car")
async def save_car(car: dict):
    car_found = await get_cars_by_license_plate(car["license_plate"])
    if car_found:
        return error_response(status=409, message="Car already exists")

    result = await create_car(car)
    if result:
        return success_response(data=result)
    return error_response(status=500, message="Something went wrong")
