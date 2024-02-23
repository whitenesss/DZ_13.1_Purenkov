from develop.class_category import Category
from develop.class_product import Product
from develop.import_json import file_json


def main():
    file = file_json()
    asd = []
    for a in file:
        for b in a['products']:
            asd.append(b)



    asddd = Product.new_product(asd[1])
    print(asddd)
    category = Category("Смартфоны", 'как средство', [asddd])
    rtyui = Product.new_product(asd[0])
    category.products = rtyui
    rtyui = Product.new_product(asd[1])
    category.products = rtyui
    rtyui = Product.new_product(asd[2])
    category.products = rtyui
    rtyui = Product.new_product(asd[3])
    category.products = rtyui
    rtyui = Product.new_product(asd[3])
    product = Product(asd[1]['name'], asd[1]['description'], asd[1]['price'], asd[1]['quantity'])

    product1 = Product(asd[2]['name'], asd[2]['description'], asd[2]['price'], asd[2]['quantity'])

    print(product + product1)
    print(asd[1],asd[2])
    print(asd[3])
    print(rtyui)
    category.products = rtyui
    category.products = rtyui
    print(category.products)
    print(asd[2])
    rtyui = Product.new_product(asd[2])
    print(rtyui)
    category.products = rtyui
    print(len(category))
    print(category, len(category))


if __name__ == '__main__':
    main()
