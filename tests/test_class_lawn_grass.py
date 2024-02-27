import pytest
from develop.class_lawn_grass import Lawn_grass
from develop.class_product import Product

from develop.class_smartphone import Smartphone


@pytest.fixture
def test_Lawn_grass():
    return Lawn_grass('test', 'test1', 1000.1, 9, 'grin', 'china', 12)

@pytest.fixture
def test_Lawn_grass_2():
    return Lawn_grass('test', 'test1', 3411.1, 4, 'grin', 'china', 12)

@pytest.fixture
def test_product():
    return Product("55\" QLED 4K", "Фоновая подсветка", 10000.0, 1, 'grin')


@pytest.fixture
def test_smartphone():
    return Smartphone('iphone', 'test1', 1000.1, 9, 'grin', 'china', 'xs', 128)




def test_init_smarthone(test_Lawn_grass):
    assert test_Lawn_grass.name == 'test'
    assert test_Lawn_grass.description == 'test1'
    assert test_Lawn_grass.request_price == 1000.1
    assert test_Lawn_grass.quantity == 9
    assert test_Lawn_grass.color == 'grin'
    assert test_Lawn_grass.germination_period == 12
    assert test_Lawn_grass.manufacturer_country == 'china'




def test_add_Lawn_grass(test_Lawn_grass, test_Lawn_grass_2):
    assert test_Lawn_grass + test_Lawn_grass_2 == 22645.3


def test_add_2(test_Lawn_grass, test_smartphone, test_product):
    assert test_Lawn_grass + test_smartphone == TypeError
    assert test_Lawn_grass + test_product == TypeError
