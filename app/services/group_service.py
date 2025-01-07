from app.db.repositories.base.base_chat_repository import BaseChatRepository
from app.db.models.core.chat import GroupModel


class GroupService:

    def __init__(self, repository: BaseChatRepository):
        self.repository = repository

    async def create_group(self, group: GroupModel):
        return await self.repository.add_group(group=group)

    async def get_group(self, group_id: str):
        group = await self.repository.get_group(group_id)
        return GroupModel(**group)

    async def update_group(self, group_data):  # UPDATE
        pass

    async def delete_group(self, group: dict):  # DELETE
        pass



