from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional
import datetime


class MongoBaseModel(BaseModel):
    id: Optional[str] = Field(alias="_id", default=None)
    created_at: Optional[datetime.datetime] = Field(default_factory=datetime.datetime.utcnow)
    updated_at: Optional[datetime.datetime] = None

    class Config:
        populate_by_name = True
        json_encoders = {ObjectId: str}
