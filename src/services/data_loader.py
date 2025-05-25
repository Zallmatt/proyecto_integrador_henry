import pandas as pd
from src.models.product import Product
from src.models.customer import Customer
from src.models.employee import Employee
from src.models.sale import Sale
from src.models.city import City
from src.models.country import Country
from src.models.category import Category

def load_products(path="data/products.csv"):
    df = pd.read_csv(path)
    return [Product(
        row['ProductID'], row['ProductName'], row['Price'], row['CategoryID'],
        row['Class'], row['ModifyDate'], row['Resistant'], row['IsAllergic'], row['VitalityDays']
    ) for _, row in df.iterrows()]

def load_customers(path="data/customers.csv"):
    df = pd.read_csv(path)
    return [Customer(
        row['CustomerID'], row['FirstName'], row['MiddleInitial'],
        row['LastName'], row['CityID'], row['Address']
    ) for _, row in df.iterrows()]

def load_employees(path="data/employees.csv"):
    df = pd.read_csv(path)
    return [Employee(
        row['EmployeeID'], row['FirstName'], row['MiddleInitial'],
        row['LastName'], row['BirthDate'], row['Gender'],
        row['CityID'], row['HireDate']
    ) for _, row in df.iterrows()]

def load_sales(path="data/sales.csv"):
    df = pd.read_csv(path)
    return [Sale(
        row['SalesID'], row['SalesPersonID'], row['CustomerID'],
        row['ProductID'], row['Quantity'], row['Discount'],
        row['TotalPrice'], row['SalesDate'], row['TransactionNumber']
    ) for _, row in df.iterrows()]

def load_cities(path="data/cities.csv"):
    df = pd.read_csv(path)
    return [City(
        row['CityID'], row['CityName'], str(row['Zipcode']).zfill(5), row['CountryID']
    ) for _, row in df.iterrows()]

def load_countries(path="data/countries.csv"):
    df = pd.read_csv(path)
    return [Country(
        row['CountryID'], row['CountryName'], row['CountryCode']
    ) for _, row in df.iterrows()]

def load_categories(path="data/categories.csv"):
    df = pd.read_csv(path)
    return [Category(
        row['CategoryID'], row['CategoryName']
    ) for _, row in df.iterrows()]
