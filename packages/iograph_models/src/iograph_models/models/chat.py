from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class Chat(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	chatType: Optional[ChatType] = Field(default=None,alias="chatType",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	isHiddenForAllMembers: Optional[bool] = Field(default=None,alias="isHiddenForAllMembers",)
	lastUpdatedDateTime: Optional[datetime] = Field(default=None,alias="lastUpdatedDateTime",)
	onlineMeetingInfo: Optional[TeamworkOnlineMeetingInfo] = Field(default=None,alias="onlineMeetingInfo",)
	tenantId: Optional[str] = Field(default=None,alias="tenantId",)
	topic: Optional[str] = Field(default=None,alias="topic",)
	viewpoint: Optional[ChatViewpoint] = Field(default=None,alias="viewpoint",)
	webUrl: Optional[str] = Field(default=None,alias="webUrl",)
	installedApps: list[TeamsAppInstallation] = Field(alias="installedApps",)
	lastMessagePreview: Optional[ChatMessageInfo] = Field(default=None,alias="lastMessagePreview",)
	members: list[ConversationMember] = Field(alias="members",)
	messages: list[ChatMessage] = Field(alias="messages",)
	permissionGrants: list[ResourceSpecificPermissionGrant] = Field(alias="permissionGrants",)
	pinnedMessages: list[PinnedChatMessageInfo] = Field(alias="pinnedMessages",)
	tabs: list[TeamsTab] = Field(alias="tabs",)

from .chat_type import ChatType
from .teamwork_online_meeting_info import TeamworkOnlineMeetingInfo
from .chat_viewpoint import ChatViewpoint
from .teams_app_installation import TeamsAppInstallation
from .chat_message_info import ChatMessageInfo
from .conversation_member import ConversationMember
from .chat_message import ChatMessage
from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
from .pinned_chat_message_info import PinnedChatMessageInfo
from .teams_tab import TeamsTab

