from pydantic import Field, EmailStr, BaseModel
from typing import List, Optional

from app.db.models.core.permissions import OwnerPermission


class BaseRole(BaseModel):

    user_id: str
    group_id: str


class OwnerRole(BaseRole):

    permissions: List[OwnerPermission]

