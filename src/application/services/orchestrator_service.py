from abc import ABC, abstractmethod


class OrchestratorService(ABC):
    @abstractmethod
    def get_functional_data(self):
        raise NotImplementedError

    @abstractmethod
    def get_api_data(self):
        raise NotImplementedError

    @abstractmethod
    def get_db_data(self):
        raise NotImplementedError
