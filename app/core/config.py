import os
from dotenv import load_dotenv

load_dotenv()


class Paths:

    MONGO_DB_URI = os.getenv("MONGO_DB_URI", "mongodb://localhost:27017")
