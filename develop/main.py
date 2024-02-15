from pprint import pprint

from develop.class_product import Category, Product
from develop.import_json import file_json


def main():
    producti_json = file_json()
    list_category = []
    list_product = []
    for categories in producti_json:
        product_catalog = [proh for proh in categories["products"]]
        category = Category(categories['name'], categories['description'], categories['products'])
        list_category.append(category.request_name())
        list_category.append(category.request_description())
        list_category.append(category.request_products())
        for categories_1 in product_catalog:
            product = Product(categories_1['name'], categories_1['description'], categories_1['price'],
                              categories_1['quantity'])
            list_product.append(product.request_name())
            list_product.append(product.request_description())
            list_product.append(product.request_price())
            list_product.append(product.request_quantity())
    print(*list_category, sep='\n')
    print()
    print(*list_product, sep='\n')

if __name__ == '__main__':
    main()
