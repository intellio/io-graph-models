# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .subscriptions import SubscriptionsRequest
	from .on_premises_synchronization import OnPremisesSynchronizationRequest
	from .federation_configurations import FederationConfigurationsRequest
	from .device_local_credentials import DeviceLocalCredentialsRequest
	from .deleted_items import DeletedItemsRequest
	from .custom_security_attribute_definitions import CustomSecurityAttributeDefinitionsRequest
	from .attribute_sets import AttributeSetsRequest
	from .administrative_units import AdministrativeUnitsRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.directory import Directory


class DirectoryRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/directory"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Directory:
		"""
		Get directory
		
		"""
		tags = ['directory.directory']

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
		return await self.request_adapter.send_async(request_info, Directory, error_mapping)

	async def patch(
		self,
		body: Directory,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Directory:
		"""
		Update directory
		
		"""
		tags = ['directory.directory']

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
		return await self.request_adapter.send_async(request_info, Directory, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	@property
	def administrative_units(self,
	) -> AdministrativeUnitsRequest:
		from .administrative_units import AdministrativeUnitsRequest
		return AdministrativeUnitsRequest(self.request_adapter, self.path_parameters)

	@property
	def attribute_sets(self,
	) -> AttributeSetsRequest:
		from .attribute_sets import AttributeSetsRequest
		return AttributeSetsRequest(self.request_adapter, self.path_parameters)

	@property
	def custom_security_attribute_definitions(self,
	) -> CustomSecurityAttributeDefinitionsRequest:
		from .custom_security_attribute_definitions import CustomSecurityAttributeDefinitionsRequest
		return CustomSecurityAttributeDefinitionsRequest(self.request_adapter, self.path_parameters)

	@property
	def deleted_items(self,
	) -> DeletedItemsRequest:
		from .deleted_items import DeletedItemsRequest
		return DeletedItemsRequest(self.request_adapter, self.path_parameters)

	@property
	def device_local_credentials(self,
	) -> DeviceLocalCredentialsRequest:
		from .device_local_credentials import DeviceLocalCredentialsRequest
		return DeviceLocalCredentialsRequest(self.request_adapter, self.path_parameters)

	@property
	def federation_configurations(self,
	) -> FederationConfigurationsRequest:
		from .federation_configurations import FederationConfigurationsRequest
		return FederationConfigurationsRequest(self.request_adapter, self.path_parameters)

	@property
	def on_premises_synchronization(self,
	) -> OnPremisesSynchronizationRequest:
		from .on_premises_synchronization import OnPremisesSynchronizationRequest
		return OnPremisesSynchronizationRequest(self.request_adapter, self.path_parameters)

	@property
	def subscriptions(self,
	) -> SubscriptionsRequest:
		from .subscriptions import SubscriptionsRequest
		return SubscriptionsRequest(self.request_adapter, self.path_parameters)

