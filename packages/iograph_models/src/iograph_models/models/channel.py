from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class Channel(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	email: Optional[str] = Field(default=None,alias="email",)
	isArchived: Optional[bool] = Field(default=None,alias="isArchived",)
	isFavoriteByDefault: Optional[bool] = Field(default=None,alias="isFavoriteByDefault",)
	membershipType: Optional[ChannelMembershipType] = Field(default=None,alias="membershipType",)
	summary: Optional[ChannelSummary] = Field(default=None,alias="summary",)
	tenantId: Optional[str] = Field(default=None,alias="tenantId",)
	webUrl: Optional[str] = Field(default=None,alias="webUrl",)
	allMembers: list[ConversationMember] = Field(alias="allMembers",)
	filesFolder: Optional[DriveItem] = Field(default=None,alias="filesFolder",)
	members: list[ConversationMember] = Field(alias="members",)
	messages: list[ChatMessage] = Field(alias="messages",)
	sharedWithTeams: list[SharedWithChannelTeamInfo] = Field(alias="sharedWithTeams",)
	tabs: list[TeamsTab] = Field(alias="tabs",)

from .channel_membership_type import ChannelMembershipType
from .channel_summary import ChannelSummary
from .conversation_member import ConversationMember
from .drive_item import DriveItem
from .conversation_member import ConversationMember
from .chat_message import ChatMessage
from .shared_with_channel_team_info import SharedWithChannelTeamInfo
from .teams_tab import TeamsTab

