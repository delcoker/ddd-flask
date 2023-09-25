from typing import Union, IO
from abc import ABC, abstractmethod


class DatabaseService(ABC):

    @abstractmethod
    def get_db(self):
        """Retrieve the initialized orm instance."""
        raise NotImplementedError
