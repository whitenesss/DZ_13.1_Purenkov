class Product:
    """Классы продукт"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @property
    def request_name(self):
        return self.name

    @property
    def request_description(self):
        return self.description

    @property
    def request_price(self):
        return self._price

    @request_price.setter
    def request_price(self, price):
        '''
        задание 4 сравниваем цены, меняем или остовляем прежнее. запрашиваем у пользователя
        '''
        if price <= 0:
            print("Цена введена не корректно")
        elif price < self._price:
            while True:
                answer = input("Новая цена ниже чем старая, вы уверены что хотите изменить цену (y/n): ").lower()
                if answer == "y":
                    self._price = price
                    break
                elif answer == "n":
                    self._price = self._price
                    break
        else:
            self._price = price

    @property
    def request_quantity(self):
        return self.quantity

    @property
    def all_request(self):
        '''Задание 3. возврощяет отбект который добовляем в список'''
        return [self.name, self.description, self.request_price, self.quantity]


