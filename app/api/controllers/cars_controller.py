from config.db_config import db_client
from utils.serializer import serialize

db_name = "cars"


async def get_all_cars():
    async with db_client() as db:
        try:
            cars = await db[db_name].find().to_list(length=100)
            return [serialize(car) for car in cars]
        except Exception as e:
            print(e)
            return None


async def get_car_by_id(id: str):
    async with db_client() as db:
        try:
            if (car := await db[db_name].find_one({"_id": id})) is not None:
                return serialize(car)
        except Exception as e:
            print(e)
            return None


async def get_cars_by_license_plate(license_plate: str):
    async with db_client() as db:
        try:
            if (
                cars := await db[db_name]
                .find({"license_plate": {"$regex": f"^{license_plate}"}})
                .to_list(length=100)
            ) is not None:
                return [serialize(car) for car in cars]
        except Exception as e:
            print(e)
            return None


async def create_car(car: dict):
    async with db_client() as db:
        try:
            result = await db[db_name].insert_one(car)
            return result.inserted_id
        except Exception as e:
            print(e)
            return None


async def update_car(id: str, car: dict):
    async with db_client() as db:
        try:
            result = await db[db_name].update_one({"_id": id}, {"$set": car})
            return result.modified_count
        except Exception as e:
            print(e)
            return None


async def delete_car(id: str):
    async with db_client() as db:
        try:
            result = await db[db_name].delete_one({"_id": id})
            return result.deleted_count
        except Exception as e:
            print(e)
            return None
