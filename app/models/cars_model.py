from pydantic import BaseModel


class Car(BaseModel):
    id: str
    license_plate: str
    is_blocked: bool
