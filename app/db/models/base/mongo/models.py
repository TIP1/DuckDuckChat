from pydantic import BaseModel, Field, field_validator
from typing import ClassVar
from bson import ObjectId
from typing import Optional, Union
import datetime


class MongoBaseModel(BaseModel):
    id: Optional[Union[str]] = Field(alias="_id", default=None)
    created_at: Optional[datetime.datetime] = Field(default_factory=datetime.datetime.utcnow)
    updated_at: Optional[datetime.datetime] = None

    @field_validator('id', mode="before")
    def check_fields(cls, value):
        if isinstance(value, ObjectId):
            return str(value)
        return value

    class Config:
        populate_by_name = True
        json_encoders = {ObjectId: str}


class MongoGroup(MongoBaseModel):
    id: Optional[Union[str]] = Field(exclude=True)
    group_id: Optional[Union[str]] = Field(default=None)

    def __init__(self, **data):
        if "_id" in data:
            data["group_id"] = str(data["_id"])
        super().__init__(**data)

