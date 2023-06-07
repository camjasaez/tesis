from pydantic import BaseModel, Field
import uuid


class Car(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    license_plate: str
    is_blocked: bool

    class Config:
        schema_extra = {
            "example": {
                "id": "00010203-0405-0607-0809-0a0b0c0d0e0f",
                "license_plate": "AA-10-00",
                "is_blocked": False,
            }
        }
