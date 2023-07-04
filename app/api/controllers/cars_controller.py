from config.db_config import db_client
from utils.serializer import serialize
from utils.error_handler import console_error_handler
from bson import ObjectId

db_name = "cars"


async def get_all_cars():
    async with db_client() as db:
        try:
            cars = await db[db_name].find().to_list(length=100)
            return [serialize(car) for car in cars]
        except Exception as e:
            console_error_handler(e, __file__, "get_all_cars")


async def get_car_by_id(id: str):
    async with db_client() as db:
        try:
            if (car := await db[db_name].find_one({"_id": ObjectId(id)})) is not None:
                return serialize(car)
        except Exception as e:
            console_error_handler(e, __file__, "get_car_by_id")


async def get_cars_by_license_plate(license_plate: str) -> list:
    async with db_client() as db:
        try:
            if (
                cars := await db[db_name]
                .find({"license_plate": {"$regex": f"^{license_plate}"}})
                .to_list(length=100)
            ) is not None:
                return [serialize(car) for car in cars] or []
        except Exception as e:
            console_error_handler(e, __file__, "get_cars_by_license_plate")


async def create_car(car: dict):
    async with db_client() as db:
        try:
            result = await db[db_name].insert_one(car)
            created_task = await db[db_name].find_one({"_id": result.inserted_id})
            return serialize(created_task)
        except Exception as e:
            console_error_handler(e, __file__, "create_car")


async def update_car(id: str, car: dict):
    async with db_client() as db:
        try:
            result = await db[db_name].update_one({"_id": id}, {"$set": car})
            return result.modified_count
        except Exception as e:
            console_error_handler(e, __file__, "update_car")


async def delete_car(id: str):
    async with db_client() as db:
        try:
            result = await db[db_name].delete_one({"_id": id})
            return result.deleted_count
        except Exception as e:
            console_error_handler(e, __file__, "delete_car")
