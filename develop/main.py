from pprint import pprint

from develop.class_product import Category, Product
from develop.import_json import file_json


def main():
    list_product_smart = []
    list_product_tv = []
    producti_json = file_json()
    for categories in producti_json:
        product_catalog = [proh for proh in categories["products"]]
        for categories_1 in product_catalog:
            if categories['name'] == 'Смартфоны':
                list_product_smart.append(categories_1['name'])
            elif categories['name'] == 'Телевизоры':
                list_product_tv.append(categories_1['name'])

    list_category = []

    for categories in producti_json:
        if categories['name'] == 'Смартфоны':
            category = Category(categories['name'], categories['description'], list_product_smart)
            list_category.append(category.request_name())
            list_category.append(category.request_description())
            list_category.append(category.request_products())
        if categories['name'] == 'Телевизоры':
            category = Category(categories['name'], categories['description'], list_product_tv)
            list_category.append(category.request_name())
            list_category.append(category.request_description())
            list_category.append(category.request_products())
    print(*list_category, sep='\n')


if __name__ == '__main__':
    main()
