class Product:
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

    @request_price.deleter
    def request_price(self):
        self._price = None

    @property
    def request_quantity(self):
        return self.quantity

    @classmethod
    def new_product(cls, product):
        '''
        Задание 3. создается товар из dict который добовляем в список
        '''
        product_list_in_categ = []
        if type(product) == dict:
            cls.name = product['name']
            cls.description = product['description']
            cls._price = product['price']
            cls.quantity = product['quantity']
            if cls.name == Product.name:
                cls.quantity += Product.quantity
                product_list_in_categ.append(cls.name)
                product_list_in_categ.append(cls.description)
                product_list_in_categ.append(cls._price)
                product_list_in_categ.append(cls.quantity)
        return product_list_in_categ
