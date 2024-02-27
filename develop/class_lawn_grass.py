from develop.class_product import Product


class Lawn_grass(Product):
    def __init__(self, name, description, price, quantity, color, manufacturer_country, germination_period):
        super().__init__(name, description, price, quantity, color)
        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period

    def __add__(self, other):
        if type(other) == Lawn_grass:
            return self.quantity * self.request_price + other.quantity * other.request_price
        return TypeError
