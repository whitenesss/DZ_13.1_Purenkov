class Category:
    """Класс категории"""
    name: str
    description: str
    products: str

    total_numbers_of_category = 0
    unique_goods = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category.total_numbers_of_category += 1
        Category.unique_goods += 1

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_products(self):
        return self.products


class Product:
    """Классы продукт"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity
