from develop.class_category import Category
from develop.class_product import Product
from develop.import_json import file_json


def main():
    file = file_json()
    asd = []
    for a in file:
        for b in a['products']:
            asd.append(b)

    asddd = Product.new_product(
        {
            "name": "Iphone 15",
            "description": "512GB, Gray space",
            "price": 210000.0,
            "quantity": 8
        })

    category = Category("Смартфоны", 'как средство', asddd)
    rtyui = Product.new_product(asd[0])
    category.products = rtyui
    rtyui = Product.new_product(asd[1])
    category.products = rtyui
    rtyui = Product.new_product(asd[2])
    category.products = rtyui
    rtyui = Product.new_product(asd[3])
    category.products = rtyui
    rtyui = Product.new_product(asd[3])
    category.products = rtyui

    print(category.products)


if __name__ == '__main__':
    main()
