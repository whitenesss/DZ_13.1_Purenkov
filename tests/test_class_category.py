import pytest
from develop.class_category import Category
from develop.class_product import Product


@pytest.fixture
def test_product():
    return Product("55\" QLED 4K", "Фоновая подсветка", 10000.0, 1, 'grin')


@pytest.fixture
def test_catgory(test_product):
    return Category('name', 'description', [test_product])


def test_init_category(test_catgory):
    assert test_catgory.name == 'name'
    assert test_catgory.description == 'description'
    first_product = test_catgory.get_product()[0]
    assert isinstance(first_product, Product)
    assert first_product.name == "55\" QLED 4K"
    assert first_product.description == "Фоновая подсветка"
    assert first_product.request_price == 10000.0
    assert first_product.quantity == 1
    assert first_product.color == 'grin'


def test_products(test_catgory, test_product):
    test_catgory.products = test_product
    assert test_catgory.products == '55" QLED 4K, 10000.0 руб. Остаток: 1 шт.\n'


def test_len(test_catgory):
    assert len(test_catgory) == 1


def test_str(test_catgory):
    assert str(test_catgory) == 'name, количество продуктов: 1'
