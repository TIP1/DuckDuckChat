import os
from dotenv import load_dotenv

from app.db.models.base.mongo.models import MongoBaseModel, MongoGroup

load_dotenv()


class SwitchModelHub:

    @staticmethod
    def get_base_model():

        db_type = os.getenv("DATABASE")

        if db_type == "MONGODB":
            return MongoBaseModel

    @staticmethod
    def get_group_model():

        db_type = os.getenv("DATABASE")

        if db_type == "MONGODB":
            return MongoGroup
