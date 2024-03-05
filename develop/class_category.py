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
        if products.quantity <= 0:
            raise ValueError
        self.__products = [products]
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
            if product.quantity <= 0:
                raise ValueError(
                    'вы пытаетесь добавить количество товара равное нулю')  # если количество товара пришло 0 то программа прерывается
            else:
                self.__products.append(product)
                Category.unique_products += 1

    def average_price(self):
        '''
        метод получения среднего ценника с условием чели товара не будет то
        возврощяем пользлвателю 'товар не добавлен'
        прогрпмма не прирывается
        '''
        try:
            aver = 0
            for product in self.__products:
                aver += product.request_price
            rezult = aver / 0
        except ZeroDivisionError:
            return 'товар не добавлен, количество равно 0'
        else:
            if rezult == 0.0:
                return 'цена равна товара ровна нулю , нужно исправить'
            else:
                return round(rezult, 2)

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
    product = Product("55\" QLED 4K", "Фоновая подсветка", 100230.0, 1, 'grin')
    category = Category('name', 'description', product)
    qwe = product.new_product(
        {'name': 'privet', 'description': 'andrey', 'price': 14000.0, 'quantity': 1, 'color': 'grin'})
    qwerr = product.new_product(
        {'name': 'privet', 'description': 'andrey', 'price': 30000.0, 'quantity': 1, 'color': 'grin'})
    category.products = qwe
    category.products = qwerr
    category.products
    print(category.average_price())
    print(category.get_product())
