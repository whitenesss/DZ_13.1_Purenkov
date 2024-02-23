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
        if products not in products:
            Category.unique_products += 1

    @property
    def products(self):
        '''вывод всего списка подученного товара'''
        result = ''
        for product in self.__products:
            print(product)
            result += f'{product.name}, {product.request_price} руб. Остаток: {product.quantity} шт.\n'
        return result
        # print(self.__products)
        # count_prod = 0
        # for i in self.__products:
        #     count_prod += 1
        #     if len(self.__products) != count_prod:
        #         print(f'{i[0]}, {i[2]} руб. Остаток: {i[3]} шт.')
        #         continue
        #     return f'{i[0]}, {i[2]} руб. Остаток: {i[3]} шт.'

    @products.setter
    def products(self, product):
        '''полученный товар добовляем в список перед этим проверяем чтобы небыло повторений'''
        if product not in self.__products:
            self.__products.append(product)

    def __len__(self):

        return len(self.__products)

    def __str__(self):
        ''' добавить строковое отображение в следующем виде:
                Смартфоны, количество продуктов: 3
        '''
        return f'{self.name}, количество продуктов:'
