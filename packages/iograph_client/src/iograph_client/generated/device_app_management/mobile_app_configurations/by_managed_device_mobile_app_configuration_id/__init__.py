# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .user_status_summary import UserStatusSummaryRequest
	from .user_statuses import UserStatusesRequest
	from .assign import AssignRequest
	from .device_status_summary import DeviceStatusSummaryRequest
	from .device_statuses import DeviceStatusesRequest
	from .assignments import AssignmentsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByManagedDeviceMobileAppConfigurationIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/deviceAppManagement/mobileAppConfigurations/{managedDeviceMobileAppConfiguration%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ManagedDeviceMobileAppConfiguration:
		"""
		Get managedDeviceMobileAppConfiguration
		Read properties and relationships of the managedDeviceMobileAppConfiguration object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-apps-manageddevicemobileappconfiguration-get?view=graph-rest-1.0
		"""
		tags = ['deviceAppManagement.managedDeviceMobileAppConfiguration']

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
		return await self.request_adapter.send_async(request_info, ManagedDeviceMobileAppConfiguration, error_mapping)

	async def patch(
		self,
		body: ManagedDeviceMobileAppConfiguration,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ManagedDeviceMobileAppConfiguration:
		"""
		Update iosMobileAppConfiguration
		Update the properties of a iosMobileAppConfiguration object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-apps-iosmobileappconfiguration-update?view=graph-rest-1.0
		"""
		tags = ['deviceAppManagement.managedDeviceMobileAppConfiguration']

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
		return await self.request_adapter.send_async(request_info, ManagedDeviceMobileAppConfiguration, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete iosMobileAppConfiguration
		Deletes a iosMobileAppConfiguration.
		Find more info here: https://learn.microsoft.com/graph/api/intune-apps-iosmobileappconfiguration-delete?view=graph-rest-1.0
		"""
		tags = ['deviceAppManagement.managedDeviceMobileAppConfiguration']
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
	def assignments(self,
	) -> AssignmentsRequest:
		from .assignments import AssignmentsRequest
		return AssignmentsRequest(self.request_adapter, self.path_parameters)

	@property
	def device_statuses(self,
	) -> DeviceStatusesRequest:
		from .device_statuses import DeviceStatusesRequest
		return DeviceStatusesRequest(self.request_adapter, self.path_parameters)

	@property
	def device_status_summary(self,
	) -> DeviceStatusSummaryRequest:
		from .device_status_summary import DeviceStatusSummaryRequest
		return DeviceStatusSummaryRequest(self.request_adapter, self.path_parameters)

	@property
	def assign(self,
	) -> AssignRequest:
		from .assign import AssignRequest
		return AssignRequest(self.request_adapter, self.path_parameters)

	@property
	def user_statuses(self,
	) -> UserStatusesRequest:
		from .user_statuses import UserStatusesRequest
		return UserStatusesRequest(self.request_adapter, self.path_parameters)

	@property
	def user_status_summary(self,
	) -> UserStatusSummaryRequest:
		from .user_status_summary import UserStatusSummaryRequest
		return UserStatusSummaryRequest(self.request_adapter, self.path_parameters)

