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
    assert test_catgory.request_name() == 'name'
    assert test_catgory.request_description() == 'description'
    assert test_catgory.request_products() == 'products'



def test_init_product(test_product):
    assert test_product.request_name() == 'name'
    assert test_product.request_description() == 'description'
    assert test_product.request_price() == 'price'
    assert test_product.request_quantity() == 'quantity'
