from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
import pandas as pd
from sqlalchemy import text

load_dotenv()

class DatabaseConnector:
    _instance = None
    _engine = None
    _Session = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnector, cls).__new__(cls)
            db_url = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
            cls._engine = create_engine(db_url, echo=False)
            cls._Session = sessionmaker(bind=cls._engine)
        return cls._instance

    def get_engine(self):
        return self._engine

    def get_session(self):
        return self._Session()

    def run_query(self, query):
        """
        Ejecuta una consulta SQL y devuelve los resultados como DataFrame de pandas.
        """
        session = self.get_session()
        result = session.execute(text(query))
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
        return df
