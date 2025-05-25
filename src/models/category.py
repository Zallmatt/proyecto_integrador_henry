class Category:
    def __init__(self, category_id, category_name):
        self.category_id = category_id
        self.category_name = category_name

    def __str__(self):
        return f"{self.category_name}"
