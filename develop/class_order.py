from develop.class_abstract_product_category_order import AbstractCategoryOrder
from develop.class_product import Product
from develop.class_mixin import ObjectCreationMixin


class Order(AbstractCategoryOrder, ObjectCreationMixin):
    '''
    Дополнительное задание
    Заказ на оплату продукта
    '''
    suppress_creation_info = False

    def __init__(self, product, quantity):
        if not isinstance(product, Product):
            raise ValueError("Product should be an instance of the Product class.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity should be a positive integer.")
        self.product = product
        self.quantity = quantity
        self.calculate_total_cost()
        if not self.suppress_creation_info:
            print((repr(self)))

    def calculate_total_cost(self):
        '''
        Получаем сумму покупки
        :return:
        '''
        self.total = self.product.request_price * self.quantity

    def __str__(self):
        '''
        Выводим сумму покупки
        :return:
        '''
        return f'Total Cost: {int(self.total)}'


if __name__ == '__main__':
    product = Product("55\" QLED 4K", "Фоновая подсветка", 10000.0, 1, 'grin')
    order = Order(product, 4)
    print(order)
