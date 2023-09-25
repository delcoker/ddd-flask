from typing import Union, IO
from abc import ABC, abstractmethod


# consumption
# - forgo a meal
# - sell asset to get access to food
# remittance

class ApiRepository(ABC):

    @abstractmethod
    def fetch_data(self):
        raise NotImplementedError
