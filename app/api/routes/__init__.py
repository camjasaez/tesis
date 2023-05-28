# Router principal
from fastapi import APIRouter
from .status_route import router as hello_router

api_router = APIRouter()

api_router.include_router(hello_router, prefix="/status", tags=["hello"])



# from fastapi import APIRouter
# from .hello import HelloRouter
#
# class Router:
#     def __init__(self):
#         self.router = APIRouter()
#         self.configure_routes()
#
#     def configure_routes(self):
#         hello_router = HelloRouter().router
#         self.router.include_router(hello_router, prefix="/hello", tags=["hello"])
#
#     def get_router(self):
#         return self.router
#
# router = Router().get_router()
