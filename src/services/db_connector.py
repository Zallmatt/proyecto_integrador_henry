from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

def get_engine():
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    database = os.getenv("DB_NAME")

    # Cadena de conexión para MySQL con SQLAlchemy
    connection_str = f"mysql+pymysql://{user}:{password}@{host}/{database}"
    engine = create_engine(connection_str)
    return engine
