from typing import Optional
from pydantic import BaseModel, Field
from bson import ObjectId


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return str(v)


class Car(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    license_plate: str
    is_blocked: bool

    class Config:
        schema_extra = {
            "example": {
                "_id": "6480ceeca860668d697482c0",
                "license_plate": "AA-10-00",
                "is_blocked": False,
            }
        }
