from abc import ABC, abstractmethod


class BaseGroupRepository(ABC):

    @abstractmethod
    def create_group(self, group) -> dict:
        pass

    @abstractmethod
    def get_group(self, group_id) -> dict:
        pass

    @abstractmethod
    def update_group(self, group_id) -> dict:
        pass

    @abstractmethod
    def delete_group(self, group_id) -> dict:
        pass
