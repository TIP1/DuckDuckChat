# from pydantic import BaseModel
from typing import Optional
from app.db.models.base.abstract.base_model import SwitchModelHub


class MessageCreate(SwitchModelHub.get_base_model()):
    sender_id: str
    chat_id: str
    content: str
    attachment_url: Optional[str] = None


class MessageResponse(SwitchModelHub.get_base_model()):
    sender_id: str
    chat_id: str
    content: str
    attachment_url: Optional[str]
    timestamp: Optional[str]
