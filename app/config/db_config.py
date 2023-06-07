from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import asynccontextmanager
from config import settings


@asynccontextmanager
async def db_client():
    mongodb_client = AsyncIOMotorClient(settings["DB_URL"])
    mongodb = mongodb_client[settings["DB_NAME"]]

    try:
        yield mongodb
    finally:
        mongodb_client.close()
