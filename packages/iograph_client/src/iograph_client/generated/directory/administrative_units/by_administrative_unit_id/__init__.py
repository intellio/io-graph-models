# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .scoped_role_members import ScopedRoleMembersRequest
	from .members import MembersRequest
	from .extensions import ExtensionsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.administrative_unit import AdministrativeUnit
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByAdministrativeUnitIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/directory/administrativeUnits/{administrativeUnit%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AdministrativeUnit:
		"""
		Get administrativeUnit
		Retrieve the properties and relationships of an administrativeUnit object.
		Find more info here: https://learn.microsoft.com/graph/api/administrativeunit-get?view=graph-rest-1.0
		"""
		tags = ['directory.administrativeUnit']

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
		return await self.request_adapter.send_async(request_info, AdministrativeUnit, error_mapping)

	async def patch(
		self,
		body: AdministrativeUnit,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AdministrativeUnit:
		"""
		Update administrativeUnit
		Update the properties of an administrativeUnit object.
		Find more info here: https://learn.microsoft.com/graph/api/administrativeunit-update?view=graph-rest-1.0
		"""
		tags = ['directory.administrativeUnit']

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
		return await self.request_adapter.send_async(request_info, AdministrativeUnit, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete administrativeUnit
		Delete an administrativeUnit.
		Find more info here: https://learn.microsoft.com/graph/api/administrativeunit-delete?view=graph-rest-1.0
		"""
		tags = ['directory.administrativeUnit']
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
	def extensions(self,
	) -> ExtensionsRequest:
		from .extensions import ExtensionsRequest
		return ExtensionsRequest(self.request_adapter, self.path_parameters)

	@property
	def members(self,
	) -> MembersRequest:
		from .members import MembersRequest
		return MembersRequest(self.request_adapter, self.path_parameters)

	@property
	def scoped_role_members(self,
	) -> ScopedRoleMembersRequest:
		from .scoped_role_members import ScopedRoleMembersRequest
		return ScopedRoleMembersRequest(self.request_adapter, self.path_parameters)

