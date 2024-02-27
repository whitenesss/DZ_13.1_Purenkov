import pytest
from develop.class_lawn_grass import Lawn_grass
from develop.class_product import Product

from develop.class_smartphone import Smartphone


@pytest.fixture
def test_Lawn_grass():
    return Lawn_grass('test', 'test1', 1000.1, 9, 'grin', 'china', 12)


@pytest.fixture
def test_product():
    return Product("55\" QLED 4K", "Фоновая подсветка", 10000.0, 1, 'grin')


@pytest.fixture
def test_smartphone():
    return Smartphone('iphone', 'test1', 1000.1, 9, 'grin', 'china', 'xs', 128)


@pytest.fixture
def test_smarthone_2():
    return Smartphone('iphone', 'test1', 5000.1, 5, 'grin', 'china', 'xs', 128)


def test_init_smarthone(test_smartphone):
    assert test_smartphone.name == 'iphone'
    assert test_smartphone.description == 'test1'
    assert test_smartphone.request_price == 1000.1
    assert test_smartphone.quantity == 9
    assert test_smartphone.color == 'grin'
    assert test_smartphone.performance == 'china'
    assert test_smartphone.model == 'xs'
    assert test_smartphone.memory == 128


def test_add_smartphone(test_smartphone, test_smarthone_2):
    assert test_smartphone + test_smarthone_2 == 34001.4


def test_add_2(test_smartphone, test_Lawn_grass, test_product):
    assert test_smartphone + test_Lawn_grass == TypeError
    assert test_smartphone + test_product == TypeError
