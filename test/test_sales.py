import sys 
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Busca en el directorio padre
from src.models.sale import Sale

def test_total_con_descuento():
    sale = Sale(
        sale_id=1,
        employee_id=101,
        customer_id=202,
        product_id=303,
        quantity=2,
        discount=0.1,  # 10% discount
        total_price=100.0,  # Total price before discount
        sale_time='2023-10-01 12:00:00',
        transaction_number='TX123456'
    )
    
    expected_total = round(100.0 * (1 - 0.1), 2)  # Expected total after discount
    assert sale.total_con_descuento() == expected_total, f"Expected {expected_total}, got {sale.total_con_descuento()}"