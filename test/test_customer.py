# tests/test_customer.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Busca en el directorio padre

from src.models.customer import Customer

def test_nombre_completo():
    cliente = Customer(1, "Ana", "M", "Gomez", 12, "Artigas 124")
    assert cliente.nombre_completo() == "Ana M. Gomez"
