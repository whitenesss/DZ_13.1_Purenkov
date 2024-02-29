import pytest

from develop.class_order import Order
from develop.class_product import Product


@pytest.fixture
def test_product():
    return Product("55\" QLED 4K", "Фоновая подсветка", 10000.0, 1, 'grin')

@pytest.fixture
def quantitiy():
    return 2

def test_init_order(test_product, quantitiy):
    assert test_product.name == "55\" QLED 4K"
    assert test_product.description == "Фоновая подсветка"
    assert test_product.request_price == 10000.0
    assert test_product.quantity == 1
    assert test_product.color == 'grin'
    assert quantitiy == 2

def test_calculate_total_cost(test_product,quantitiy):
    order = Order(test_product, quantitiy)
    order.calculate_total_cost()
    assert order.total == 20000.0

def test_calculate_total_cost_1(test_product):
    with pytest.raises(ValueError, match="Quantity should be a positive integer."):
        order = Order(test_product, 0)