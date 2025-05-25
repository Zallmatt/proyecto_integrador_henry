import pandas as pd
from src.services.db_connector import get_engine

def insert_products(products):
    df = pd.DataFrame([vars(p) for p in products])
    df.to_sql("products", con=get_engine(), if_exists="append", index=False)

def insert_customers(customers):
    df = pd.DataFrame([vars(c) for c in customers])
    df.to_sql("customers", con=get_engine(), if_exists="append", index=False)

def insert_employees(employees):
    df = pd.DataFrame([vars(e) for e in employees])
    df.to_sql("employees", con=get_engine(), if_exists="append", index=False)

def insert_sales(sales):
    df = pd.DataFrame([vars(s) for s in sales])
    df.to_sql("sales", con=get_engine(), if_exists="append", index=False)

def insert_cities(cities):
    df = pd.DataFrame([vars(c) for c in cities])
    df.to_sql("cities", con=get_engine(), if_exists="append", index=False)

def insert_countries(countries):
    df = pd.DataFrame([vars(c) for c in countries])
    df.to_sql("countries", con=get_engine(), if_exists="append", index=False)

def insert_categories(categories):
    df = pd.DataFrame([vars(c) for c in categories])
    df.to_sql("categories", con=get_engine(), if_exists="append", index=False)
