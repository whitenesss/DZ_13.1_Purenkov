class Category:
    """Класс категории"""
    name: str
    description: str
    products: list
    total_numbers_of_category = 0
    unique_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        # if products not in Category.products:
        #      Category.products.append(products)
        Category.total_numbers_of_category += 1
        Category.unique_products += len(products)

    def request_name(self):
        return self.name

    def request_description(self):
        return self.description

    def request_products(self):
        '''задание 1 приватный атрибут roduct'''
        return self.__products

    @property
    def request_description_1(self):
        '''
        задание 2  выводить список товаров в формате:
        Продукт, 80 руб. Остаток: 15 шт.
        '''
        return f'{self.__products[0]}, {self.__products[2]} руб. Остаток: {self.__products[3]} шт.'

    @request_description_1.setter
    def request_description_1(self, product):
        self.__products = product
