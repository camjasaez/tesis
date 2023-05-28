from pydantic import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

def get_common_settings() -> dict:
    return {
        "APP_NAME": "Detector-app",
        "DEBUG_MODE": False,
    }

def get_server_settings() -> dict:
    port = os.getenv("PORT")
    host = os.getenv("HOST")
    return {
        "HOST": "0.0.0.0",
        "PORT": 8000,
    }

def get_database_settings() -> dict:
    db_url = os.getenv("DB_URL")
    db_name = os.getenv("DB_NAME")

    return {
        "DB_URL": db_url,
        "DB_NAME": db_name,
    }

def get_settings() -> dict:
    settings = {}
    settings.update(get_common_settings())
    settings.update(get_server_settings())
    settings.update(get_database_settings())
    print(settings)
    return settings

settings = get_settings()

# from pydantic import BaseSettings
# from dotenv import load_dotenv
#
# load_dotenv()
#
# class CommonSettings(BaseSettings):
#     APP_NAME: str = "Detector-app"
#     DEBUG_MODE: bool = False
#
#
# class ServerSettings(BaseSettings):
#     HOST: str = "0.0.0.0"
#     PORT: int = 8000
#
#
# class DatabaseSettings(BaseSettings):
#     DB_URL: str
#     DB_NAME: str
#
#
# class Settings(CommonSettings, ServerSettings, DatabaseSettings):
#     pass
#
#
# settings = Settings()
