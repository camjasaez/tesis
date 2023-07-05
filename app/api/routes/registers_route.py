from fastapi import APIRouter
from typing import Annotated, Union
from api.controllers.registers_controller import (
    get_all_registers,
    get_register_by_id,
    create_register,
)
from api.controllers.cars_controller import (
    get_cars_by_license_plate,
    create_car,
)

from utils.responses import success_response, error_response
from models.registers_model import Register

# /registers
router = APIRouter()


@router.get("/", response_description="Get all registers")
async def get_all():
    registers = await get_all_registers()
    if registers:
        return success_response(data=registers)
    if registers.__len__() == 0:
        return error_response(status=204, message="No registers")
    return error_response(status=500, message="Something went wrong")


@router.get("/{id}", response_description="Get register by id")
async def get_by_id(id: str):
    register = await get_register_by_id(id)
    if register:
        return success_response(data=register)
    return error_response(status=500, message="Something went wrong")


@router.post("/", response_description="Create register")
async def save_register(register: dict):
    register_found = await get_cars_by_license_plate(register["license_plate"])
    if register_found == []:
        result = await create_car({"license_plate": register["license_plate"]})
        id_car = result["_id"]
        new_register = await create_register(register, id_car)
        if new_register:
            return success_response(data=new_register)
        return error_response(status=500, message="Something went wrong")

    id_car = register_found[0]["_id"]

    new_register = await create_register(register, id_car)
    if new_register:
        return success_response(data=new_register)
    return error_response(status=500, message="Something went wrong")
