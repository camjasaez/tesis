from config.env_config import ENV_VARIABLES
from pymongo.mongo_client import MongoClient

# conexión a la base de datos
# Obtiene el valor de la variable de entorno DB_HOST
MONGO_URL = ENV_VARIABLES["MONGO_URL"]


def connect_db():
    client = MongoClient(MONGO_URL)
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
