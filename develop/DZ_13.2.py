from develop.class_category import Category
from develop.class_product import Product
from develop.import_json import file_json


def main():
    list_product_smart = []
    list_product_tv = []
    name_category = []
    description_category = []
    producti_json = file_json()
    for cat in producti_json:
        if cat['name'] == 'Смартфоны':
            name_category.append(cat['name'])
            description_category.append(cat['description'])
            for i in cat['products']:
                product = Product(i['name'], i['description'], i['price'], i['quantity'])
                list_product_smart.append(product.all_request)
        if cat['name'] == 'Телевизоры':
            name_category.append(cat['name'])
            description_category.append(cat['description'])
            for i in cat['products']:
                product = Product(i['name'], i['description'], i['price'], i['quantity'])
                list_product_tv.append(product.all_request)

    category = Category(name_category[0], description_category[0], list_product_smart[2])
    print(category.request_description_1)
    category.request_description_1 = list_product_tv[0]
    print(category.request_description_1)
    product = Product(list_product_smart[0][0], list_product_smart[0][1], list_product_smart[0][2],
                      list_product_smart[0][3])
    print(product.request_price)
    product.request_price = 0
    print(product.request_price)


if __name__ == '__main__':
    main()
