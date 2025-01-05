from bson import ObjectId
import asyncio

from app.db.repositories.base.base_chat_repository import BaseChatRepository
from app.db.repositories.base.base_user_repository import BaseUserRepository
from app.db.models.core.user import UserModel

class MongoUserRepository(BaseUserRepository):

    def __init__(self, db_client):
        self.collection = db_client.DuckDuckChat_Atlas.users

    async def add_user(self, user: UserModel):
        result = await self.collection.insert_one(user.dict())
        return str(result.inserted_id)

    async def get_user(self, user_id: str):
        result = await self.collection.find_one({"_id": ObjectId(user_id)})
        return result

    async def update_user(self, user_data):
        pass

    async def delete_user(self, user: dict):
        pass

    async def get_users_by_role(self, role: str) -> list:
        pass

    async def add_friend(self, user_id: str, friend_id: str) -> dict:
        pass

    async def is_friend(self, user_id: str, friend_id: str) -> bool:
        pass

    async def delete_friend(self, user_id: str, friend_id: str) -> dict:
        pass
