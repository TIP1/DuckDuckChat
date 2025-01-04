from abc import ABC, abstractmethod


class BaseChatRepository(ABC):

    @abstractmethod
    def create_chat(self, chat_name, owner) -> dict:
        pass

    @abstractmethod
    def get_chat(self, chat_id) -> dict:
        pass

    @abstractmethod
    def update_chat(self, chat_id) -> dict:
        pass

    @abstractmethod
    def delete_chat(self, chat_id) -> dict:
        pass
