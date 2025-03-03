# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_host_pair_id import ByHostPairIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.security_host_pair_collection_response import SecurityHostPairCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ChildHostPairsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/threatIntelligence/hosts/{host%2Did}/childHostPairs", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecurityHostPairCollectionResponse:
		"""
		List childHostPairs
		Get the list of hostPair resources associated with a host, where that host is the *parent* and has an outgoing pairing to a *child*. 
		Find more info here: https://learn.microsoft.com/graph/api/security-host-list-childhostpairs?view=graph-rest-1.0
		"""
		tags = ['security.threatIntelligence']

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
		return await self.request_adapter.send_async(request_info, SecurityHostPairCollectionResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> ChildHostPairsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ChildHostPairsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ChildHostPairsRequest(self.request_adapter, self.path_parameters)

	def by_host_pair_id(self,
		host_id: str,
		hostPair_id: str,
	) -> ByHostPairIdRequest:
		if host_id is None:
			raise TypeError("host_id cannot be null.")
		if hostPair_id is None:
			raise TypeError("hostPair_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["host%2Did"] =  host_id
		path_parameters["hostPair%2Did"] =  hostPair_id

		from .by_host_pair_id import ByHostPairIdRequest
		return ByHostPairIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

