# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .disconnect import DisconnectRequest
	from .begin_onboarding import BeginOnboardingRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.remote_assistance_partner import RemoteAssistancePartner


class ByRemoteAssistancePartnerIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/deviceManagement/remoteAssistancePartners/{remoteAssistancePartner%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> RemoteAssistancePartner:
		"""
		Get remoteAssistancePartner
		Read properties and relationships of the remoteAssistancePartner object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-remoteassistance-remoteassistancepartner-get?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.remoteAssistancePartner']

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
		return await self.request_adapter.send_async(request_info, RemoteAssistancePartner, error_mapping)

	async def patch(
		self,
		body: RemoteAssistancePartner,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> RemoteAssistancePartner:
		"""
		Update remoteAssistancePartner
		Update the properties of a remoteAssistancePartner object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-remoteassistance-remoteassistancepartner-update?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.remoteAssistancePartner']

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
		return await self.request_adapter.send_async(request_info, RemoteAssistancePartner, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete remoteAssistancePartner
		Deletes a remoteAssistancePartner.
		Find more info here: https://learn.microsoft.com/graph/api/intune-remoteassistance-remoteassistancepartner-delete?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.remoteAssistancePartner']
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
	def begin_onboarding(self,
	) -> BeginOnboardingRequest:
		from .begin_onboarding import BeginOnboardingRequest
		return BeginOnboardingRequest(self.request_adapter, self.path_parameters)

	@property
	def disconnect(self,
	) -> DisconnectRequest:
		from .disconnect import DisconnectRequest
		return DisconnectRequest(self.request_adapter, self.path_parameters)

