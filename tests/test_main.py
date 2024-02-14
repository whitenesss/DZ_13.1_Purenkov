import pytest
from develop.class_product import Category
from develop.class_product import Product



@pytest.fixture
def test_catgory():
    return Category('name', 'description', 'products')


@pytest.fixture
def test_product():
    return Product('name', 'description', 'price','quantity')


def test_init_category(test_catgory):
    assert test_catgory.get_name() == 'name'
    assert test_catgory.get_description() == 'description'
    assert test_catgory.get_products() == 'products'



def test_init_product(test_product):
    assert test_product.get_name() == 'name'
    assert test_product.get_description() == 'description'
    assert test_product.get_price() == 'price'
    assert test_product.get_quantity() == 'quantity'
