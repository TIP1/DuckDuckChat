from pydantic import BaseModel, Field, field_validator
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


class MongoBaseModelRequest(MongoBaseModel):
    id: Optional[str] = Field(alias="_id", default=None)


# class MongoBaseModelResponse(MongoBaseModel):
#     id: Optional[ObjectId] = Field(alias="_id", default=None)
