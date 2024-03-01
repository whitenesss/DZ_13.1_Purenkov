from develop.class_product import Product
from develop.class_abstract_product_category_order import AbstractCategoryOrder
from develop.class_mixin import ObjectCreationMixin


class Category(AbstractCategoryOrder, ObjectCreationMixin):
    '''
    Класс категорий товаров
    '''
    suppress_creation_info = False
    category_count = 0
    unique_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        if products not in self.__products:
            Category.unique_products += 1
        if not self.suppress_creation_info:
            print((repr(self)))

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
        if isinstance(product,
                      Product) and product not in self.__products:  # проверяем что приходит точно из класса продукт
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

if __name__ == '__main__':
    product = Product("55\" QLED 4K", "Фоновая подсветка", 10000.0, 1, 'grin')
    category = Category('name', 'description', [product])

