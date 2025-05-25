from src.models.sale import Sale

def test_total_with_discount():
    sale = Sale(
        sale_id=1,
        employee_id=1,
        customer_id=1,
        product_id=1,
        quantity=2,
        discount=0.1,  # 10%
        total_price=100,
        sale_time="12:00",
        transaction_number="ABC123"
    )
    assert sale.total_with_discount() == 90.0
