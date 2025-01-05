from app.db.repositories.base.base_user_repository import BaseUserRepository
from app.db.models.core.user import UserModel


class UserService:

    def __init__(self, repository: BaseUserRepository):
        self.repository = repository

    async def add_user(self, user: UserModel):
        return await self.repository.add_user(user=user)

    async def get_user(self, user_id: str):
        user = await self.repository.get_user(user_id)
        return UserModel(**user)

    async def update_user(self, user_data):  # UPDATE
        pass

    async def delete_user(self, user: dict):  # DELETE
        pass

    async def get_users_by_role(self, role: str) -> list:
        pass

    async def add_friend(self, user_id: str, friend_id: str) -> dict:
        pass

    async def is_friend(self, user_id: str, friend_id: str) -> bool:
        pass

    async def delete_friend(self, user_id: str, friend_id: str) -> dict:
        pass

