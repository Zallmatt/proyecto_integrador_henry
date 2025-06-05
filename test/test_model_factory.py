from src.factories.model_factory import ModelFactory
from src.models.customer import Customer
import pytest

def test_create_customer_from_row():
    row = {
        "CustomerID": 1,
        "FirstName": "Matias",
        "MiddleInitial": "F",
        "LastName": "Zalazar",
        "CityID": 101,
        "Address": "Belgrano 111"
    }

    customer = ModelFactory.create_customer(row)
    assert isinstance(customer, Customer)
    assert customer._first_name == "Matias"
    assert customer._address == "Belgrano 111"

def test_create_customer_missing_field():
    row = {
        "CustomerID": 1,
        "FirstName": "Matias"
        # faltan campos requeridos como LastName, CityID, Address, etc.
    }

    with pytest.raises(KeyError):
        ModelFactory.create_customer(row)