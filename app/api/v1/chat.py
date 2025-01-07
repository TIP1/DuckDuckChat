from fastapi import FastAPI, APIRouter

from app.db.repositories.repository_factory import RepositoryFactory
from app.services.group_service import GroupService
from app.db.models.core.chat import GroupModel


group_router = APIRouter()
group_repository = RepositoryFactory.get_group_repository()
group_service = GroupService(group_repository)


@group_router.post("/create")
async def add_group(group_data: dict):
    result = await group_service.add_group(GroupModel(**group_data))
    return {"message": f"New group {result} added successfully!"}


@group_router.get("/{group_id}")
async def get_group(group_id: str):
    group = await group_service.get_group(group_id)
    return {"GET Group": f"{group}"}

