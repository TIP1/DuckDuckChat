from pydantic import Field, EmailStr, BaseModel
from typing import List, Optional


class BasePermission(BaseModel):

    pass


class OwnerPermission(BasePermission):

    pass


class AdminPermission(BasePermission):
    pass


class ChatMemberPermission(BasePermission):
    pass


class ChannelMemberPermission(BasePermission):
    pass

