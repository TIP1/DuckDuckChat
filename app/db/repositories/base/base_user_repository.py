from abc import ABC, abstractmethod


class BaseUserRepository(ABC):

    @abstractmethod
    def add_user(self, user: dict):  # CREATE
        pass

    @abstractmethod
    def get_user(self, user_id: str):  # READ
        pass

    @abstractmethod
    def update_user(self, user_data):  # UPDATE
        pass

    @abstractmethod
    def delete_user(self, user: dict):  # DELETE
        pass

    @abstractmethod
    def get_users_by_role(self, role: str) -> list:
        pass

    @abstractmethod
    def add_friend(self, user_id: str, friend_id: str) -> dict:
        pass

    @abstractmethod
    def is_friend(self, user_id: str, friend_id: str) -> bool:
        pass

    @abstractmethod
    def delete_friend(self, user_id: str, friend_id: str) -> dict:
        pass
