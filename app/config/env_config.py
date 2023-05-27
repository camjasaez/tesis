from dotenv import load_dotenv
import os

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Obtiene el valor de la variable de entorno DB_HOST


ENV_VARIABLES = {
    "MONGO_URL": os.getenv("MONGO_URL"),
}

