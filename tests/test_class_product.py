import pytest
from develop.class_product import Product


@pytest.fixture
def test_product():
    return Product("55\" QLED 4K", "Фоновая подсветка", 10000.0, 1)


def test_init_product(test_product):
    assert test_product.request_name == "55\" QLED 4K"
    assert test_product.request_description == "Фоновая подсветка"
    assert test_product.request_price == 10000.0
    assert test_product.request_quantity == 1
    # assert test_product.create_product({"name": "HUAWEI P60", "description": "Инновационный изогнутый экран",
    #                                       "price": 62_000.0, "quantity": 19}) == '<develop.class_product.Product object at 0x000002677BC72690>'
