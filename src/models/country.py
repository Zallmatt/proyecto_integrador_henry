class Country:
    def __init__(self, country_id, country_name, country_code):
        self.country_id = country_id
        self.country_name = country_name
        self.country_code = country_code

    def __str__(self):
        return f"{self.country_name} ({self.country_code})"
