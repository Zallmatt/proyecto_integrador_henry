from src.models.customer import Customer

def test_customer_full_name():
    customer = Customer(
        customer_id=1,
        first_name="Ana",
        middle_initial="M",
        last_name="Gomez",
        city_id=10,
        address="123 Main St"
    )
    assert customer.full_name() == "Ana M. Gomez"
