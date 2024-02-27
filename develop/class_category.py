from develop.class_product import Product
class Category:
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
        if isinstance(product, Product):# проверяем что приходит точно из класса продукт
            if product not in self.__products:
                self.__products.append(product)

    def get_product(self):
        return self.__products
    def __len__(self) -> object:

        return len(self.__products)

    def __str__(self):
        ''' добавить строковое отображение в следующем виде:
                Смартфоны, количество продуктов: 3
        '''
        return f'{self.name}, количество продуктов: {Category.__len__(self)}'
