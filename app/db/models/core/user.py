from pydantic import Field, EmailStr
from typing import List, Optional

from app.db.models.base.abstract.base_model import SwitchModelHub


class UserModel(SwitchModelHub.get_base_model()):

    username: Optional[str] = Field(..., min_length=3, max_length=50, description="Username")
    email: Optional[EmailStr] = None  # pkg: email-validator
    roles: List[str]


