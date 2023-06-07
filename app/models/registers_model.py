from pydantic import BaseModel, Field
from datetime import datetime
import uuid


class Register(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    type: str
    date: datetime
    prediction_accuracy: float
    vehicle_image: str
    license_plate_image: str
    vehicle_id: str

    class Config:
        schemma_extra = {
            "example": {
                "id": "11111213-1415-1617-1819-1a1b1c1d1e1f",
                "type": "entry",
                "date": "2021-01-01T00:00:00",
                "prediction_accuracy": 0.9,
                "vehicle_image": "https://i.imgur.com/1.jpg",
                "license_plate_image": "https://i.imgur.com/2.jpg",
                "vehicle_id": "00010203-0405-0607-0809-0a0b0c0d0e0f",
            }
        }
