class Product:

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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

    @property
    def request_quantity(self):
        return self.quantity

    @classmethod
    def new_product(cls, product_data: dict):
        '''
        Задание 3. создается товар из dict который добовляем в список
        '''

        return cls(**product_data)

    def __str__(self):
        '''Задание 1: строковое отображение ввиде ниже представленном'''
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт'

    def __add__(self, other):
        '''
        Задание 2
        '''
        return self.quantity * self.__price + other.quantity * other.__price
