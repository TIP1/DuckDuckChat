import os
from dotenv import load_dotenv

from app.db.models.base.mongo.base_model import MongoBaseModel

load_dotenv()


class SwitchModelHub:

    @staticmethod
    def get_base_model():

        db_type = os.getenv("DATABASE")

        if db_type == "MONGODB":
            return MongoBaseModel

    @staticmethod
    def get_another_model():
        pass
