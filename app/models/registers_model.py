from typing import Optional
from pydantic import BaseModel, Field
from bson import ObjectId
from datetime import datetime


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return str(v)


class Register(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    type: str
    date: datetime
    prediction_accuracy: float
    vehicle_image: str
    license_plate_image: str
    vehicle_id: str

    class Config:
        schemma_extra = {
            "example": {
                "_id": "6486262eaf888e26ad176f41",
                "type": "entry",
                "date": "2021-01-01T00:00:00",
                "prediction_accuracy": 0.9,
                "vehicle_image": "https://i.imgur.com/1.jpg",
                "license_plate_image": "https://i.imgur.com/2.jpg",
                "vehicle_id": "00010203-0405-0607-0809-0a0b0c0d0e0f",
            }
        }
