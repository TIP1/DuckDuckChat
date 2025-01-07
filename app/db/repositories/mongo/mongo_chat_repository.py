from app.db.repositories.base.base_chat_repository import BaseChatRepository


class MongoGroupRepository(BaseChatRepository):

    def __init__(self, db_client):
        self.collection = db_client.DuckDuckChat_Atlas.groups

    async def create_chat(self, chat_name, owner) -> dict:
        pass

    async def get_chat(self, chat_id) -> dict:
        pass

    async def update_chat(self, chat_id) -> dict:
        pass

    async def delete_chat(self, chat_id) -> dict:
        pass