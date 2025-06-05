from src.database.db_connector import DatabaseConnector
import pandas as pd

def test_singleton_instance():
    db1 = DatabaseConnector()
    db2 = DatabaseConnector()
    assert db1 is db2, "DatabaseConnector no cumple con Singleton"

def test_run_query_returns_dataframe():
    db = DatabaseConnector()
    df = db.run_query("SELECT * FROM categories LIMIT 1")
    assert isinstance(df, pd.DataFrame)
    assert not df.empty