import pytest
from src.models.product import Product

def test_product_is_perishable():
    product = Product(
        product_id=1,
        name="Milk",
        price=10.99,
        category_id=2,
        product_class="Medium",
        modify_time="12:00",
        resistant="Durable",
        is_allergic="Unknown",
        vitality_days=7
    )

    assert product.is_perishable() is True
