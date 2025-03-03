# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .replies import RepliesRequest
	from .unset_reaction import UnsetReactionRequest
	from .undo_soft_delete import UndoSoftDeleteRequest
	from .soft_delete import SoftDeleteRequest
	from .set_reaction import SetReactionRequest
	from .hosted_contents import HostedContentsRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.chat_message import ChatMessage
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByChatMessageIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/teams/{team%2Did}/primaryChannel/messages/{chatMessage%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ChatMessage:
		"""
		Get messages from teams
		A collection of all the messages in the channel. A navigation property. Nullable.
		"""
		tags = ['teams.channel']

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
		return await self.request_adapter.send_async(request_info, ChatMessage, error_mapping)

	async def patch(
		self,
		body: ChatMessage,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ChatMessage:
		"""
		Update the navigation property messages in teams
		
		"""
		tags = ['teams.channel']

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
		return await self.request_adapter.send_async(request_info, ChatMessage, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property messages for teams
		
		"""
		tags = ['teams.channel']
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



	def with_url(self, raw_url: str) -> ByChatMessageIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByChatMessageIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByChatMessageIdRequest(self.request_adapter, self.path_parameters)

	@property
	def hosted_contents(self,
	) -> HostedContentsRequest:
		from .hosted_contents import HostedContentsRequest
		return HostedContentsRequest(self.request_adapter, self.path_parameters)

	@property
	def set_reaction(self,
	) -> SetReactionRequest:
		from .set_reaction import SetReactionRequest
		return SetReactionRequest(self.request_adapter, self.path_parameters)

	@property
	def soft_delete(self,
	) -> SoftDeleteRequest:
		from .soft_delete import SoftDeleteRequest
		return SoftDeleteRequest(self.request_adapter, self.path_parameters)

	@property
	def undo_soft_delete(self,
	) -> UndoSoftDeleteRequest:
		from .undo_soft_delete import UndoSoftDeleteRequest
		return UndoSoftDeleteRequest(self.request_adapter, self.path_parameters)

	@property
	def unset_reaction(self,
	) -> UnsetReactionRequest:
		from .unset_reaction import UnsetReactionRequest
		return UnsetReactionRequest(self.request_adapter, self.path_parameters)

	@property
	def replies(self,
	) -> RepliesRequest:
		from .replies import RepliesRequest
		return RepliesRequest(self.request_adapter, self.path_parameters)

