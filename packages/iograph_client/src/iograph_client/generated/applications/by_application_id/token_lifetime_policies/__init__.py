# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .ref import RefRequest
	from .count import CountRequest
	from .by_token_lifetime_policy_id import ByTokenLifetimePolicyIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.token_lifetime_policy_collection_response import TokenLifetimePolicyCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class TokenLifetimePoliciesRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/applications/{application%2Did}/tokenLifetimePolicies"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> TokenLifetimePolicyCollectionResponse:
		"""
		List assigned tokenLifetimePolicies
		List the tokenLifetimePolicy objects that are assigned to an application. Only one object is returned in the collection because only one tokenLifetimePolicy can be assigned to an application.
		Find more info here: https://learn.microsoft.com/graph/api/application-list-tokenlifetimepolicies?view=graph-rest-1.0
		"""
		tags = ['applications.tokenLifetimePolicy']

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
		return await self.request_adapter.send_async(request_info, TokenLifetimePolicyCollectionResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	@property
	def by_token_lifetime_policy_id(self,
	) -> ByTokenLifetimePolicyIdRequest:
		from .by_token_lifetime_policy_id import ByTokenLifetimePolicyIdRequest
		return ByTokenLifetimePolicyIdRequest(self.request_adapter, self.path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def ref(self,
	) -> RefRequest:
		from .ref import RefRequest
		return RefRequest(self.request_adapter, self.path_parameters)

