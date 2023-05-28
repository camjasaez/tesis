from fastapi import APIRouter

router = APIRouter()

@router.get("/", response_description="Hello World")
def read_root():
    return {"Status": "Online","Message": "Happy Coding! 📚💻"}




# from fastapi import APIRouter
#
# class HelloRouter:
#     def __init__(self):
#         self.router = APIRouter()
#         self.configure_routes()
#
#     def configure_routes(self):
#         @self.router.get("/")
#         async def hello():
#             return {"message": "Hello, World!"}
