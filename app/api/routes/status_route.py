from fastapi import APIRouter

router = APIRouter()


@router.get("/", response_description="Hello World")
def read_root():
    return {"Status": "Online", "Message": "Happy Coding! 📚💻"}
