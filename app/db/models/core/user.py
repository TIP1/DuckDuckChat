from bson import ObjectId
from pydantic import Field, EmailStr, BaseModel, field_validator
from typing import List, Optional, Union

# from app.db.models.base.abstract.base_model import SwitchModelHub


class CreateUser:

    @staticmethod
    class Request(BaseModel):
        username: Optional[str] = Field(..., min_length=3, max_length=50, description="Username")
        email: Optional[EmailStr] = None  # pkg: email-validator

    @staticmethod
    class Response(BaseModel):
        id: Optional[Union[str]] = Field(alias="_id", default=None)
        username: Optional[str] = Field(..., min_length=3, max_length=50, description="Username")
        email: Optional[EmailStr] = None  # pkg: email-validator

        @field_validator('id', mode="before")
        def check_fields(cls, value):
            if isinstance(value, ObjectId):
                return str(value)
            return value

        class Config:
            populate_by_name = True
            json_encoders = {ObjectId: str}

class GroupMember(BaseModel):
    user_id: str
    group_id: str
    roles: List[str]
    permissions: List[str]
