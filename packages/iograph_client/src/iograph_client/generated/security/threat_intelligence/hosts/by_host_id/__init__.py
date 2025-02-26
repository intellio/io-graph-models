# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .whois import WhoisRequest
	from .trackers import TrackersRequest
	from .subdomains import SubdomainsRequest
	from .ssl_certificates import SslCertificatesRequest
	from .reputation import ReputationRequest
	from .ports import PortsRequest
	from .passive_dns_reverse import PassiveDnsReverseRequest
	from .passive_dns import PassiveDnsRequest
	from .parent_host_pairs import ParentHostPairsRequest
	from .host_pairs import HostPairsRequest
	from .cookies import CookiesRequest
	from .components import ComponentsRequest
	from .child_host_pairs import ChildHostPairsRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.security_host import SecurityHost


class ByHostIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/security/threatIntelligence/hosts/{host%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecurityHost:
		"""
		Get host
		Read the properties and relationships of a host object. The host resource is the abstract base type that returns an implementation. A host can be of one of the following types:
		Find more info here: https://learn.microsoft.com/graph/api/security-host-get?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, SecurityHost, error_mapping)

	async def patch(
		self,
		body: SecurityHost,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SecurityHost:
		"""
		Update the navigation property hosts in security
		
		"""
		tags = ['security.threatIntelligence']

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
		return await self.request_adapter.send_async(request_info, SecurityHost, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property hosts for security
		
		"""
		tags = ['security.threatIntelligence']
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
	def child_host_pairs(self,
	) -> ChildHostPairsRequest:
		from .child_host_pairs import ChildHostPairsRequest
		return ChildHostPairsRequest(self.request_adapter, self.path_parameters)

	@property
	def components(self,
	) -> ComponentsRequest:
		from .components import ComponentsRequest
		return ComponentsRequest(self.request_adapter, self.path_parameters)

	@property
	def cookies(self,
	) -> CookiesRequest:
		from .cookies import CookiesRequest
		return CookiesRequest(self.request_adapter, self.path_parameters)

	@property
	def host_pairs(self,
	) -> HostPairsRequest:
		from .host_pairs import HostPairsRequest
		return HostPairsRequest(self.request_adapter, self.path_parameters)

	@property
	def parent_host_pairs(self,
	) -> ParentHostPairsRequest:
		from .parent_host_pairs import ParentHostPairsRequest
		return ParentHostPairsRequest(self.request_adapter, self.path_parameters)

	@property
	def passive_dns(self,
	) -> PassiveDnsRequest:
		from .passive_dns import PassiveDnsRequest
		return PassiveDnsRequest(self.request_adapter, self.path_parameters)

	@property
	def passive_dns_reverse(self,
	) -> PassiveDnsReverseRequest:
		from .passive_dns_reverse import PassiveDnsReverseRequest
		return PassiveDnsReverseRequest(self.request_adapter, self.path_parameters)

	@property
	def ports(self,
	) -> PortsRequest:
		from .ports import PortsRequest
		return PortsRequest(self.request_adapter, self.path_parameters)

	@property
	def reputation(self,
	) -> ReputationRequest:
		from .reputation import ReputationRequest
		return ReputationRequest(self.request_adapter, self.path_parameters)

	@property
	def ssl_certificates(self,
	) -> SslCertificatesRequest:
		from .ssl_certificates import SslCertificatesRequest
		return SslCertificatesRequest(self.request_adapter, self.path_parameters)

	@property
	def subdomains(self,
	) -> SubdomainsRequest:
		from .subdomains import SubdomainsRequest
		return SubdomainsRequest(self.request_adapter, self.path_parameters)

	@property
	def trackers(self,
	) -> TrackersRequest:
		from .trackers import TrackersRequest
		return TrackersRequest(self.request_adapter, self.path_parameters)

	@property
	def whois(self,
	) -> WhoisRequest:
		from .whois import WhoisRequest
		return WhoisRequest(self.request_adapter, self.path_parameters)

