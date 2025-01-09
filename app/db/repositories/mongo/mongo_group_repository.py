from app.db.models.core.group import GroupModel

from app.db.repositories.base.base_group_repository import BaseGroupRepository


class MongoGroupRepository(BaseGroupRepository):

    def __init__(self, db_client):
        self.collection = db_client.DuckDuckChat_Atlas.groups

    async def create_group(self, group: GroupModel):
        result = await self.collection.insert_one(group.dict())
        return result

    async def get_group(self, group_id) -> GroupModel:
        group = await self.collection.find_one({"group_id": group_id})
        return GroupModel(**group)

    async def update_group(self, group_id) -> bool:
        pass

    async def delete_group(self, group_id) -> bool:
        pass
