class Sale:
    def __init__(self, sale_id, employee_id, customer_id, product_id, quantity, discount, total_price, sale_time, transaction_number):
        self.sale_id = sale_id
        self.employee_id = employee_id
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity
        self.discount = discount
        self.total_price = total_price
        self.sale_time = sale_time
        self.transaction_number = transaction_number

    def total_with_discount(self):
        return round(self.total_price * (1 - self.discount), 2)

    def __str__(self):
        return f"Sale #{self.sale_id}: ${self.total_price} at {self.sale_time}"
