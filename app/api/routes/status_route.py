from fastapi import APIRouter
from api.controllers.status_controller import status as get_status

router = APIRouter()


@router.get("/", response_description="Hello World")
async def status():
    return await get_status()
