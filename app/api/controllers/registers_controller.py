from config.db_config import db_client
from utils.serializer import serialize
from utils.error_handler import console_error_handler
from bson import ObjectId
import datetime

db_name = "registers"


async def get_all_registers():
    async with db_client() as db:
        try:
            registers = await db[db_name].find().to_list(length=100)
            return [serialize(register) for register in registers]
        except Exception as e:
            console_error_handler(e, __file__, "get_all_registers")


async def get_register_by_id(id: str):
    async with db_client() as db:
        try:
            if (
                register := await db[db_name].find_one({"_id": ObjectId(id)})
            ) is not None:
                return serialize(register)
        except Exception as e:
            console_error_handler(e, __file__, "get_register_by_id")


async def create_register(register: dict, vehicle_id: str):
    async with db_client() as db:
        try:
            register["vehicle_id"] = vehicle_id
            register["date"] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            result = await db[db_name].insert_one(register)
            created_task = await db[db_name].find_one({"_id": result.inserted_id})
            return serialize(created_task)
        except Exception as e:
            console_error_handler(e, __file__, "create_register")
