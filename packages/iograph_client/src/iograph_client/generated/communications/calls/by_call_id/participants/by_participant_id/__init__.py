# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .stop_hold_music import StopHoldMusicRequest
	from .start_hold_music import StartHoldMusicRequest
	from .mute import MuteRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.participant import Participant
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByParticipantIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/communications/calls/{call%2Did}/participants/{participant%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Participant:
		"""
		Get participant
		Retrieve the properties and relationships of a participant object.
		Find more info here: https://learn.microsoft.com/graph/api/participant-get?view=graph-rest-1.0
		"""
		tags = ['communications.call']

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
		return await self.request_adapter.send_async(request_info, Participant, error_mapping)

	async def patch(
		self,
		body: Participant,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Participant:
		"""
		Update the navigation property participants in communications
		
		"""
		tags = ['communications.call']

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
		return await self.request_adapter.send_async(request_info, Participant, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete participant
		Delete a specific participant in a call. In some situations, it is appropriate for an application to remove a participant from an active call. This action can be done before or after the participant answers the call. When an active caller is removed, they are immediately dropped from the call with no pre- or post-removal notification. When an invited participant is removed, any outstanding add participant request is canceled. 
		Find more info here: https://learn.microsoft.com/graph/api/participant-delete?view=graph-rest-1.0
		"""
		tags = ['communications.call']
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



	@property
	def mute(self,
	) -> MuteRequest:
		from .mute import MuteRequest
		return MuteRequest(self.request_adapter, self.path_parameters)

	@property
	def start_hold_music(self,
	) -> StartHoldMusicRequest:
		from .start_hold_music import StartHoldMusicRequest
		return StartHoldMusicRequest(self.request_adapter, self.path_parameters)

	@property
	def stop_hold_music(self,
	) -> StopHoldMusicRequest:
		from .stop_hold_music import StopHoldMusicRequest
		return StopHoldMusicRequest(self.request_adapter, self.path_parameters)

