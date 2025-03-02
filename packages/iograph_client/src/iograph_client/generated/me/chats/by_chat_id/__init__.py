# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .tabs import TabsRequest
	from .pinned_messages import PinnedMessagesRequest
	from .permission_grants import PermissionGrantsRequest
	from .unhide_for_user import UnhideForUserRequest
	from .send_activity_notification import SendActivityNotificationRequest
	from .mark_chat_unread_for_user import MarkChatUnreadForUserRequest
	from .mark_chat_read_for_user import MarkChatReadForUserRequest
	from .hide_for_user import HideForUserRequest
	from .messages import MessagesRequest
	from .members import MembersRequest
	from .last_message_preview import LastMessagePreviewRequest
	from .installed_apps import InstalledAppsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.chat import Chat
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByChatIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/chats/{chat%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Chat:
		"""
		Get chats from me
		
		"""
		tags = ['me.chat']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.GET,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_async(request_info, Chat, error_mapping)

	async def patch(
		self,
		body: Chat,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Chat:
		"""
		Update the navigation property chats in me
		
		"""
		tags = ['me.chat']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.PATCH,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, Chat, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property chats for me
		
		"""
		tags = ['me.chat']
		header_parameters = [{'name': 'If-Match', 'in': 'header', 'description': 'ETag', 'schema': {'type': 'string'}}]

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.DELETE,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")



	def with_url(self, raw_url: str) -> ByChatIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByChatIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByChatIdRequest(self.request_adapter, self.path_parameters)

	@property
	def installed_apps(self,
	) -> InstalledAppsRequest:
		from .installed_apps import InstalledAppsRequest
		return InstalledAppsRequest(self.request_adapter, self.path_parameters)

	@property
	def last_message_preview(self,
	) -> LastMessagePreviewRequest:
		from .last_message_preview import LastMessagePreviewRequest
		return LastMessagePreviewRequest(self.request_adapter, self.path_parameters)

	@property
	def members(self,
	) -> MembersRequest:
		from .members import MembersRequest
		return MembersRequest(self.request_adapter, self.path_parameters)

	@property
	def messages(self,
	) -> MessagesRequest:
		from .messages import MessagesRequest
		return MessagesRequest(self.request_adapter, self.path_parameters)

	@property
	def hide_for_user(self,
	) -> HideForUserRequest:
		from .hide_for_user import HideForUserRequest
		return HideForUserRequest(self.request_adapter, self.path_parameters)

	@property
	def mark_chat_read_for_user(self,
	) -> MarkChatReadForUserRequest:
		from .mark_chat_read_for_user import MarkChatReadForUserRequest
		return MarkChatReadForUserRequest(self.request_adapter, self.path_parameters)

	@property
	def mark_chat_unread_for_user(self,
	) -> MarkChatUnreadForUserRequest:
		from .mark_chat_unread_for_user import MarkChatUnreadForUserRequest
		return MarkChatUnreadForUserRequest(self.request_adapter, self.path_parameters)

	@property
	def send_activity_notification(self,
	) -> SendActivityNotificationRequest:
		from .send_activity_notification import SendActivityNotificationRequest
		return SendActivityNotificationRequest(self.request_adapter, self.path_parameters)

	@property
	def unhide_for_user(self,
	) -> UnhideForUserRequest:
		from .unhide_for_user import UnhideForUserRequest
		return UnhideForUserRequest(self.request_adapter, self.path_parameters)

	@property
	def permission_grants(self,
	) -> PermissionGrantsRequest:
		from .permission_grants import PermissionGrantsRequest
		return PermissionGrantsRequest(self.request_adapter, self.path_parameters)

	@property
	def pinned_messages(self,
	) -> PinnedMessagesRequest:
		from .pinned_messages import PinnedMessagesRequest
		return PinnedMessagesRequest(self.request_adapter, self.path_parameters)

	@property
	def tabs(self,
	) -> TabsRequest:
		from .tabs import TabsRequest
		return TabsRequest(self.request_adapter, self.path_parameters)

