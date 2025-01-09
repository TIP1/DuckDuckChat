import os
from dotenv import load_dotenv

# from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient

from app.db.repositories.mongo.mongo_user_repository import MongoUserRepository
from app.db.repositories.mongo.mongo_group_repository import MongoGroupRepository


load_dotenv()


class RepositoryFactory:

    @staticmethod
    def get_user_repository():

        db_type = os.getenv("DATABASE")

        if db_type == "MONGODB":
            uri = os.getenv("URI_MONGO_DB")
            client = AsyncIOMotorClient(uri)

            return MongoUserRepository(client)

    @staticmethod
    def get_group_repository():

        db_type = os.getenv("DATABASE")

        if db_type == "MONGODB":
            uri = os.getenv("URI_MONGO_DB")
            client = AsyncIOMotorClient(uri)

            return MongoGroupRepository(client)

