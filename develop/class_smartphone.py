from develop.class_product import Product


class Smartphone(Product):
    def __init__(self,name, description, price, quantity, color, performance,model,memory):
        super().__init__(name, description, price, quantity, color)
        self.performance = performance
        self.model = model
        self.memory = memory

    def __add__(self, other):
        if type(other) == Smartphone:
            return self.quantity * self.request_price + other.quantity * other.request_price
        return TypeError
