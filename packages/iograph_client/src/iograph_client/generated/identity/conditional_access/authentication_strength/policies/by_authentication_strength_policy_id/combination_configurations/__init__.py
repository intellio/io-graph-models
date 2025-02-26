# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_authentication_combination_configuration_id import ByAuthenticationCombinationConfigurationIdRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.models.authentication_combination_configuration_collection_response import AuthenticationCombinationConfigurationCollectionResponse
from iograph_models.models.authentication_combination_configuration import AuthenticationCombinationConfiguration
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class CombinationConfigurationsRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/identity/conditionalAccess/authenticationStrength/policies/{authenticationStrengthPolicy%2Did}/combinationConfigurations"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AuthenticationCombinationConfigurationCollectionResponse:
		"""
		List combinationConfigurations
		Get the authenticationCombinationConfiguration objects for an authentication strength policy. The objects can be of one or more of the following derived types:
* fido2combinationConfigurations
* x509certificatecombinationconfiguration authenticationCombinationConfiguration objects are supported only for custom authentication strengths.
		Find more info here: https://learn.microsoft.com/graph/api/authenticationstrengthpolicy-list-combinationconfigurations?view=graph-rest-1.0
		"""
		tags = ['identity.conditionalAccessRoot']

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
		return await self.request_adapter.send_async(request_info, AuthenticationCombinationConfigurationCollectionResponse, error_mapping)

	async def post(
		self,
		body: AuthenticationCombinationConfiguration,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AuthenticationCombinationConfiguration:
		"""
		Create authenticationCombinationConfiguration
		Create a new authenticationCombinationConfiguration object which can be of one of the following derived types:
* fido2combinationConfiguration
* x509certificatecombinationconfiguration
		Find more info here: https://learn.microsoft.com/graph/api/authenticationstrengthpolicy-post-combinationconfigurations?view=graph-rest-1.0
		"""
		tags = ['identity.conditionalAccessRoot']

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
		return await self.request_adapter.send_async(request_info, AuthenticationCombinationConfiguration, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def by_authentication_combination_configuration_id(self,
		authenticationStrengthPolicy_id: str,
		authenticationCombinationConfiguration_id: str,
	) -> ByAuthenticationCombinationConfigurationIdRequest:
		if authenticationStrengthPolicy_id is None:
			raise TypeError("authenticationStrengthPolicy_id cannot be null.")
		if authenticationCombinationConfiguration_id is None:
			raise TypeError("authenticationCombinationConfiguration_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["authenticationStrengthPolicy%2Did"] =  authenticationStrengthPolicy_id
		path_parameters["authenticationCombinationConfiguration%2Did"] =  authenticationCombinationConfiguration_id

		from .by_authentication_combination_configuration_id import ByAuthenticationCombinationConfigurationIdRequest
		return ByAuthenticationCombinationConfigurationIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

