from config.db_config import db_client
from utils.serializer import serialize


async def get_all_cars():
    async with db_client() as db:
        try:
            cars = await db["cars"].find().to_list(length=100)
            return [serialize(car) for car in cars]
        except Exception as e:
            print(e)
            return None


async def get_car_by_id(id: str):
    async with db_client() as db:
        try:
            car = await db["cars"].find_one({"_id": id})
            return serialize(car)
        except Exception as e:
            print(e)
            return None


async def create_car(car: dict):
    async with db_client() as db:
        try:
            result = await db["cars"].insert_one(car)
            return result.inserted_id
        except Exception as e:
            print(e)
            return None


async def update_car(id: str, car: dict):
    async with db_client() as db:
        try:
            result = await db["cars"].update_one({"_id": id}, {"$set": car})
            return result.modified_count
        except Exception as e:
            print(e)
            return None


async def delete_car(id: str):
    async with db_client() as db:
        try:
            result = await db["cars"].delete_one({"_id": id})
            return result.deleted_count
        except Exception as e:
            print(e)
            return None
