# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .owners import OwnersRequest
	from .group import GroupRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.community import Community


class ByCommunityIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/employeeExperience/communities/{community%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Community:
		"""
		Get community
		Read the properties and relationships of a community object.
		Find more info here: https://learn.microsoft.com/graph/api/community-get?view=graph-rest-1.0
		"""
		tags = ['employeeExperience.community']

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
		return await self.request_adapter.send_async(request_info, Community, error_mapping)

	async def patch(
		self,
		body: Community,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Community:
		"""
		Update community
		Update the properties of an existing Viva Engage community.
		Find more info here: https://learn.microsoft.com/graph/api/community-update?view=graph-rest-1.0
		"""
		tags = ['employeeExperience.community']

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
		return await self.request_adapter.send_async(request_info, Community, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete community
		Delete a Viva Engage community along with all associated Microsoft 365 content, including the connected Microsoft 365 group, OneNote notebook, and Planner plans. For more information, see What happens if I delete a Viva Engage community connected to Microsoft 365 groups.
		Find more info here: https://learn.microsoft.com/graph/api/community-delete?view=graph-rest-1.0
		"""
		tags = ['employeeExperience.community']
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
	def group(self,
	) -> GroupRequest:
		from .group import GroupRequest
		return GroupRequest(self.request_adapter, self.path_parameters)

	@property
	def owners(self,
	) -> OwnersRequest:
		from .owners import OwnersRequest
		return OwnersRequest(self.request_adapter, self.path_parameters)

