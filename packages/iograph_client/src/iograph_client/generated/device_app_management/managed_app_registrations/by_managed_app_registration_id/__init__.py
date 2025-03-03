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
	from .operations import OperationsRequest
	from .intended_policies import IntendedPoliciesRequest
	from .applied_policies import AppliedPoliciesRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.managed_app_registration import ManagedAppRegistration
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByManagedAppRegistrationIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceAppManagement/managedAppRegistrations/{managedAppRegistration%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ManagedAppRegistration:
		"""
		Get iosManagedAppRegistration
		Read properties and relationships of the iosManagedAppRegistration object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-mam-iosmanagedappregistration-get?view=graph-rest-1.0
		"""
		tags = ['deviceAppManagement.managedAppRegistration']

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
		return await self.request_adapter.send_async(request_info, ManagedAppRegistration, error_mapping)

	async def patch(
		self,
		body: ManagedAppRegistration,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ManagedAppRegistration:
		"""
		Update the navigation property managedAppRegistrations in deviceAppManagement
		
		"""
		tags = ['deviceAppManagement.managedAppRegistration']

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
		return await self.request_adapter.send_async(request_info, ManagedAppRegistration, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property managedAppRegistrations for deviceAppManagement
		
		"""
		tags = ['deviceAppManagement.managedAppRegistration']
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



	def with_url(self, raw_url: str) -> ByManagedAppRegistrationIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByManagedAppRegistrationIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByManagedAppRegistrationIdRequest(self.request_adapter, self.path_parameters)

	@property
	def applied_policies(self,
	) -> AppliedPoliciesRequest:
		from .applied_policies import AppliedPoliciesRequest
		return AppliedPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def intended_policies(self,
	) -> IntendedPoliciesRequest:
		from .intended_policies import IntendedPoliciesRequest
		return IntendedPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def operations(self,
	) -> OperationsRequest:
		from .operations import OperationsRequest
		return OperationsRequest(self.request_adapter, self.path_parameters)

