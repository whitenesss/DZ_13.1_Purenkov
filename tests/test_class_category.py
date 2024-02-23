import pytest
from develop.class_category import Category


@pytest.fixture
def test_catgory():
    return Category('name', 'description',         [{'name': 'Xiaomi Redmi Note 11', 'description': '1024GB, Синий', 'price': 31000.0, 'quantity': 14}])


def test_init_category(test_catgory):
    assert test_catgory.name == 'name'
    assert test_catgory.description == 'description'
    # assert test_catgory.products != 'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт'


# def test_f_category(test_catgory):
#     assert test_catgory.request_description_1 == '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.'
#     assert test_catgory.unique_products == 8
#     assert test_catgory.total_numbers_of_category == 2
