from abc import ABC, abstractmethod


class AbstractProduct(ABC):
    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def new_product(self):
        pass


class AbstractCategoryOrder(ABC):

    @abstractmethod
    def calculate_total_cost(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
