# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_device_management_exchange_connector_id import ByDeviceManagementExchangeConnectorIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.device_management_exchange_connector_collection_response import DeviceManagementExchangeConnectorCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.device_management_exchange_connector import DeviceManagementExchangeConnector


class ExchangeConnectorsRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/deviceManagement/exchangeConnectors"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceManagementExchangeConnectorCollectionResponse:
		"""
		List deviceManagementExchangeConnectors
		List properties and relationships of the deviceManagementExchangeConnector objects.
		Find more info here: https://learn.microsoft.com/graph/api/intune-onboarding-devicemanagementexchangeconnector-list?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.deviceManagementExchangeConnector']

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
		return await self.request_adapter.send_async(request_info, DeviceManagementExchangeConnectorCollectionResponse, error_mapping)

	async def post(
		self,
		body: DeviceManagementExchangeConnector,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceManagementExchangeConnector:
		"""
		Create deviceManagementExchangeConnector
		Create a new deviceManagementExchangeConnector object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-onboarding-devicemanagementexchangeconnector-create?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.deviceManagementExchangeConnector']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.POST,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, DeviceManagementExchangeConnector, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def by_device_management_exchange_connector_id(self,
		deviceManagementExchangeConnector_id: str,
	) -> ByDeviceManagementExchangeConnectorIdRequest:
		if deviceManagementExchangeConnector_id is None:
			raise TypeError("deviceManagementExchangeConnector_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementExchangeConnector%2Did"] =  deviceManagementExchangeConnector_id

		from .by_device_management_exchange_connector_id import ByDeviceManagementExchangeConnectorIdRequest
		return ByDeviceManagementExchangeConnectorIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

