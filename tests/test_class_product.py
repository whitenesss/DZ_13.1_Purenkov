import pytest

from develop.class_product import Product
from unittest.mock import patch


@pytest.fixture
def test_product():
    return Product("55\" QLED 4K", "Фоновая подсветка", 10000.0, 1, 'grin')


@pytest.fixture
def test_product_2():
    return Product("55\" QLED 4K", "Фоновая подсветка", 20000.0, 2, 'grin')


def test_init_product(test_product):
    assert test_product.name == "55\" QLED 4K"
    assert test_product.description == "Фоновая подсветка"
    assert test_product.request_price == 10000.0
    assert test_product.quantity == 1
    assert test_product.color == 'grin'


def test_prise(monkeypatch, test_product):
    assert test_product.request_price == 10000.0
    user_input = 'y'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    test_product.request_price = 100
    assert test_product.request_price == 100


def test_prise_n(monkeypatch, test_product):
    user_input = 'n'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    test_product.request_price = 100
    assert test_product.request_price == 10000.0


def test_prise_y(monkeypatch, test_product):
    user_input = '0'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    monkeypatch.setattr('builtins.input', lambda _: 'y')
    test_product.request_price = 100
    assert test_product.request_price == 100
    del test_product.request_price
    assert test_product.request_price == None


def test_new_product(test_product):
    new_product_instance = test_product.new_product(
        {'name': 'Iphone 15', 'description': '512GB, Gray space', 'price': 210000.0,
         'quantity': 8, 'color': 'grin'})
    assert str(new_product_instance) == 'Iphone 15, 210000.0 руб. Остаток: 8 шт'


def test_add(test_product, test_product_2):
    assert test_product + test_product_2 == 50000.0

