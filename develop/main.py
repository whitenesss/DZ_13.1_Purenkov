
from develop.class_category import Category
from develop.class_product import Product
from develop.import_json import file_json


def main():
    producti_json = file_json()
    list_product_smart = []
    list_product_tv = []
    for categories in producti_json:
        product_catalog = [proh for proh in categories["products"]]
        for categories_1 in product_catalog:
            print(categories_1)
            if categories['name'] == 'Смартфоны':
                list_product_smart.append(categories_1)
                # list_product_smart.append(categories_1['description'])
                # list_product_smart.append(categories_1['price'])
                # list_product_smart.append(categories_1['quantity'])
            elif categories['name'] == 'Телевизоры':
                list_product_tv.append(categories_1)


    for categories in producti_json:
        if categories['name'] == 'Смартфоны':
            category = Category(categories['name'], categories['description'], list_product_smart)



if __name__ == '__main__':
    main()
