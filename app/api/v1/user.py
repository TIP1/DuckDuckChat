import asyncio

from fastapi import FastAPI, APIRouter


from app.db.repositories.repository_factory import RepositoryFactory
from app.services.user_service import UserService
from app.db.models.core.user import UserModel


user_router = APIRouter()
user_repository = RepositoryFactory.get_user_repository()
user_service = UserService(user_repository)


@user_router.post("/create")
async def add_user(user_data: dict):
    result = await user_service.add_user(UserModel(**user_data))
    return {"message": f"New user {result} added successfully!"}


@user_router.get("/{user_id}")
async def get_user(user_id: str):
    user = await user_service.get_user(user_id)
    await asyncio.sleep(5)
    return {"GET User": f"{user}"}

