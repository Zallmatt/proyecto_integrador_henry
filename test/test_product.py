import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Busca en el directorio padre
from src.models.product import Product

def test_product_precio_final():
    product = Product(1, "PC", 1500, 1, "Electronics", "2023-10-01", True, False, 30)
    assert product.precio_final() == 1500.00