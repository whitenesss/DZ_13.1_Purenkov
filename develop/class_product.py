class Category:
    """Класс категории"""
    name: str
    description: str
    products: []

    total_numbers_of_category = 0
    unique_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category.total_numbers_of_category += 1
        Category.unique_products += len(products)

    def request_name(self):
        return self.name

    def request_description(self):
        return self.description

    def request_products(self):
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

    def request_name(self):
        return self.name

    def request_description(self):
        return self.description

    def request_price(self):
        return self.price

    def request_quantity(self):
        return self.quantity
