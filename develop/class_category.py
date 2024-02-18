class Category:
    '''
    Класс категорий товаров
    '''
    category_count = 0
    unique_products = 1

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = [products]
        Category.category_count += 1
        if products not in products:
            Category.unique_products += 1

    @property
    def products_1(self):
        return self.__products
    @property
    def products(self):
        '''вывод всего списка подученного товара'''
        # print(self.__products)
        count_prod = 0
        for i in self.__products:
            count_prod += 1
            if len(self.__products) != count_prod:
                print(f'{i[0]}, {i[2]} руб. Остаток: {i[3]} шт.')
                continue
            return f'{i[0]}, {i[2]} руб. Остаток: {i[3]} шт.'

    @products.setter
    def products(self, product):
        '''полученный товар добовляем в список перед этим проверяем чтобы небыло повторений'''
        if product not in self.__products:
            self.__products.append(product)
