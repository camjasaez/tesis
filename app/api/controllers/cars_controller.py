from config.db_config import db_client
from utils.serializer import serialize


async def get_all_cars():
    async with db_client() as db:
        cars = await db["cars"].find().to_list(length=100)
        return [serialize(car) for car in cars]
