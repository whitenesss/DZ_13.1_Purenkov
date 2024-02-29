from develop.class_product import Product


class Lawn_grass(Product, ):
    suppress_creation_info = True

    def __init__(self, name, description, price, quantity, color, manufacturer_country, germination_period):
        super().__init__(name, description, price, quantity, color)
        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period
        print(f"{repr(self)}")

    def __add__(self, other):
        if type(other) == Lawn_grass:
            return self.quantity * self.request_price + other.quantity * other.request_price
        return TypeError

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт'


if __name__ == '__main__':
    lawn_grass = Lawn_grass('test', 'test1', 1000.1, 9, 'grin', 'china', 12)
