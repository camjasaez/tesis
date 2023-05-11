from env_config import ENV_VARIABLES
from pymongo import MongoClient

# conexión a la base de datos
# Obtiene el valor de la variable de entorno DB_HOST
MONGO_URL = ENV_VARIABLES["MONGO_URL"]
MONGO_DB = ENV_VARIABLES["MONGO_DB"]


def connect_db():
    try:
        # Crea una instancia del cliente de MongoDB
        client = MongoClient(MONGO_URL)
        db = client[MONGO_DB]
        return db

    except Exception as e:
        print(e)
        return None
