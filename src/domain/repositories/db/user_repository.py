from abc import ABC, abstractmethod


class UserRepository(ABC):

    @abstractmethod
    def get_all_users(self):
        raise NotImplementedError
