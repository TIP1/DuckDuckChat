from app.db.models.base.abstract.base_model import SwitchModelHub
from typing import Optional, List


class GroupModel(SwitchModelHub.get_base_model()):

    group_id: Optional[str]
    group_name: str
    group_owner_id: str
    group_admins: List[str]
    group_members: List[str]


class ChatModel(GroupModel):
    pass


class ChannelModel(GroupModel):
    pass
