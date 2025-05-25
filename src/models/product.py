class Product:
    def __init__(self, product_id, name, price, category_id, product_class, modify_time, resistant, is_allergic, vitality_days):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category_id = category_id
        self.product_class = product_class
        self.modify_time = modify_time
        self.resistant = resistant
        self.is_allergic = is_allergic
        self.vitality_days = vitality_days

    def is_perishable(self):
        return self.vitality_days > 0

    def __str__(self):
        return f"{self.name} (${self.price})"
