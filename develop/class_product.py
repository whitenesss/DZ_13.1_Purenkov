from develop.class_abstract_product_category_order import AbstractProduct
from develop.class_mixin import ObjectCreationMixin


class Product(AbstractProduct, ObjectCreationMixin):
    color: str
    suppress_creation_info = False

    def __init__(self, name, description, price, quantity, color):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.color = color
        if not self.suppress_creation_info:
            print((repr(self)))

    @property
    def request_price(self):
        return self.__price

    @request_price.setter
    def request_price(self, price):
        '''
        задание 4 сравниваем цены, меняем или остовляем прежнее. запрашиваем у пользователя
        '''
        if price <= 0:
            print("Цена введена не корректно")
        elif price < self.__price:
            while True:
                answer = input("Новая цена ниже чем старая, вы уверены что хотите изменить цену (y/n): ").lower()
                if answer == "y":
                    self.__price = price
                    break
                elif answer == "n":
                    self.__price = self.__price
                    break
        else:
            self.__price = price

    @request_price.deleter
    def request_price(self):
        self.__price = None

    @classmethod
    def new_product(cls, product_data: dict):
        '''
        Задание 3. создается товар из dict который добовляем в список
        '''
        valid_keys = {'name', 'description', 'price', 'quantity', 'color'}
        filtered_data = {key: product_data[key] for key in valid_keys if key in product_data}
        return cls(**filtered_data)

    def __str__(self):
        '''Задание 1: строковое отображение ввиде ниже представленном'''
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт'

    def __add__(self, other):
        '''
        Задание 2
        '''
        if isinstance(other, Product):
            return self.quantity * self.request_price + other.quantity * other.request_price
        return TypeError


if __name__ == '__main__':
    product = Product("55\" QLED 4K", "Фоновая подсветка", 10000.0, 1, 'grin')
