from develop.class_product import Product


class Smartphone(Product):
    suppress_creation_info = True

    def __init__(self, name, description, price, quantity, color, performance, model, memory):
        super().__init__(name, description, price, quantity, color)
        self.performance = performance
        self.model = model
        self.memory = memory
        print(repr(self))

    def __add__(self, other):
        if type(other) == Smartphone:
            return self.quantity * self.request_price + other.quantity * other.request_price
        return TypeError

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт'


if __name__ == '__main__':
    smartphone = Smartphone('iphone', 'test1', 1000.1, 9, 'grin', 'china', 'xs', 128)
