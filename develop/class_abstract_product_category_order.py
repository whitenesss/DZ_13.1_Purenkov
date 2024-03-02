from abc import ABC, abstractmethod


class AbstractProduct(ABC):
    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_data: dict):
        pass


class AbstractCategoryOrder(ABC):

    @abstractmethod
    def calculate_total_cost(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
