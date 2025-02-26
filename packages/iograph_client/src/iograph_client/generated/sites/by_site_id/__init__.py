# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .term_stores import TermStoresRequest
	from .term_store import TermStoreRequest
	from .sites import SitesRequest
	from .permissions import PermissionsRequest
	from .pages import PagesRequest
	from .operations import OperationsRequest
	from .onenote import OnenoteRequest
	from .lists import ListsRequest
	from .last_modified_by_user import LastModifiedByUserRequest
	from .items import ItemsRequest
	from .external_columns import ExternalColumnsRequest
	from .drives import DrivesRequest
	from .drive import DriveRequest
	from .created_by_user import CreatedByUserRequest
	from .content_types import ContentTypesRequest
	from .columns import ColumnsRequest
	from .analytics import AnalyticsRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.site import Site


class BySiteIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/sites/{site%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Site:
		"""
		Get a site resource
		Retrieve properties and relationships for a site resource.
A site resource represents a team site in SharePoint.
		Find more info here: https://learn.microsoft.com/graph/api/site-get?view=graph-rest-1.0
		"""
		tags = ['sites.site']

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
		return await self.request_adapter.send_async(request_info, Site, error_mapping)

	async def patch(
		self,
		body: Site,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Site:
		"""
		Update entity in sites
		
		"""
		tags = ['sites.site']

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
		return await self.request_adapter.send_async(request_info, Site, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	@property
	def analytics(self,
	) -> AnalyticsRequest:
		from .analytics import AnalyticsRequest
		return AnalyticsRequest(self.request_adapter, self.path_parameters)

	@property
	def columns(self,
	) -> ColumnsRequest:
		from .columns import ColumnsRequest
		return ColumnsRequest(self.request_adapter, self.path_parameters)

	@property
	def content_types(self,
	) -> ContentTypesRequest:
		from .content_types import ContentTypesRequest
		return ContentTypesRequest(self.request_adapter, self.path_parameters)

	@property
	def created_by_user(self,
	) -> CreatedByUserRequest:
		from .created_by_user import CreatedByUserRequest
		return CreatedByUserRequest(self.request_adapter, self.path_parameters)

	@property
	def drive(self,
	) -> DriveRequest:
		from .drive import DriveRequest
		return DriveRequest(self.request_adapter, self.path_parameters)

	@property
	def drives(self,
	) -> DrivesRequest:
		from .drives import DrivesRequest
		return DrivesRequest(self.request_adapter, self.path_parameters)

	@property
	def external_columns(self,
	) -> ExternalColumnsRequest:
		from .external_columns import ExternalColumnsRequest
		return ExternalColumnsRequest(self.request_adapter, self.path_parameters)

	@property
	def items(self,
	) -> ItemsRequest:
		from .items import ItemsRequest
		return ItemsRequest(self.request_adapter, self.path_parameters)

	@property
	def last_modified_by_user(self,
	) -> LastModifiedByUserRequest:
		from .last_modified_by_user import LastModifiedByUserRequest
		return LastModifiedByUserRequest(self.request_adapter, self.path_parameters)

	@property
	def lists(self,
	) -> ListsRequest:
		from .lists import ListsRequest
		return ListsRequest(self.request_adapter, self.path_parameters)

	@property
	def onenote(self,
	) -> OnenoteRequest:
		from .onenote import OnenoteRequest
		return OnenoteRequest(self.request_adapter, self.path_parameters)

	@property
	def operations(self,
	) -> OperationsRequest:
		from .operations import OperationsRequest
		return OperationsRequest(self.request_adapter, self.path_parameters)

	@property
	def pages(self,
	) -> PagesRequest:
		from .pages import PagesRequest
		return PagesRequest(self.request_adapter, self.path_parameters)

	@property
	def permissions(self,
	) -> PermissionsRequest:
		from .permissions import PermissionsRequest
		return PermissionsRequest(self.request_adapter, self.path_parameters)

	@property
	def sites(self,
	) -> SitesRequest:
		from .sites import SitesRequest
		return SitesRequest(self.request_adapter, self.path_parameters)

	@property
	def term_store(self,
	) -> TermStoreRequest:
		from .term_store import TermStoreRequest
		return TermStoreRequest(self.request_adapter, self.path_parameters)

	@property
	def term_stores(self,
	) -> TermStoresRequest:
		from .term_stores import TermStoresRequest
		return TermStoresRequest(self.request_adapter, self.path_parameters)

