# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .post_federation_signup import PostFederationSignupRequest
	from .post_attribute_collection import PostAttributeCollectionRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.user_flow_api_connector_configuration import UserFlowApiConnectorConfiguration
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ApiConnectorConfigurationRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/identity/b2xUserFlows/{b2xIdentityUserFlow%2Did}/apiConnectorConfiguration"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> UserFlowApiConnectorConfiguration:
		"""
		Get userFlowApiConnectorConfiguration
		Get the apiConnectorConfiguration property in a b2xIdentityUserFlow to detail the API connectors enabled for the user flow.
		Find more info here: https://learn.microsoft.com/graph/api/b2xidentityuserflow-get-apiconnectorconfiguration?view=graph-rest-1.0
		"""
		tags = ['identity.b2xIdentityUserFlow']

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
		return await self.request_adapter.send_async(request_info, UserFlowApiConnectorConfiguration, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	@property
	def post_attribute_collection(self,
	) -> PostAttributeCollectionRequest:
		from .post_attribute_collection import PostAttributeCollectionRequest
		return PostAttributeCollectionRequest(self.request_adapter, self.path_parameters)

	@property
	def post_federation_signup(self,
	) -> PostFederationSignupRequest:
		from .post_federation_signup import PostFederationSignupRequest
		return PostFederationSignupRequest(self.request_adapter, self.path_parameters)

