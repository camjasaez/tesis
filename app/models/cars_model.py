from pydantic import BaseModel


class Car(BaseModel):
    license_plate: str
    is_blocked: bool

    class Config:
        schema_extra = {
            "example": {
                "_id": "00010203-0405-0607-0809-0a0b0c0d0e0f",
                "license_plate": "AA-10-00",
                "is_blocked": False,
            }
        }
