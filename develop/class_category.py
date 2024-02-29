from develop.class_product import Product
from develop.class_abstract_product_category_order import AbstractCategoryOrder


class Category(AbstractCategoryOrder):
    '''
    Класс категорий товаров
    '''
    category_count = 0
    unique_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        if products not in self.__products:
            Category.unique_products += 1

    @property
    def products(self):
        '''вывод всего списка подученного товара'''
        result = ''
        for product in self.__products:
            print(product)
            result += f'{product.name}, {product.request_price} руб. Остаток: {product.quantity} шт.\n'
        return result

    @products.setter
    def products(self, product):
        '''полученный товар добовляем в список перед этим проверяем чтобы небыло повторений'''
        if isinstance(product, Product) and product not in self.__products:  # проверяем что приходит точно из класса продукт
            self.__products.append(product)
            Category.unique_products += 1

    def calculate_total_cost(self):
        pass

    def get_product(self):
        return self.__products

    def __len__(self) -> object:

        return len(self.__products)

    def __str__(self):
        ''' добавить строковое отображение в следующем виде:
                Смартфоны, количество продуктов: 3
        '''
        return f'{self.name}, количество продуктов: {len(self)}'
