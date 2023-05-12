from dotenv import load_dotenv
import os

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Obtiene el valor de la variable de entorno DB_HOST


ENV_VARIABLES = {
    "MONGO_HOST": os.getenv("MONGO_HOST"),
    "MONGO_PORT": os.getenv("MONGO_PORT"),
    "MONGO_USER": os.getenv("MONGO_USER"),
    "MONGO_PASS": os.getenv("MONGO_PASS"),
    "MONGO_DB": os.getenv("MONGO_DB"),
    "MONGO_TEST_DB": os.getenv("MONGO_TEST_DB"),
    "MONGO_URL": os.getenv("MONGO_URL"),
}

print(ENV_VARIABLES)

