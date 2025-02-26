# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .special import SpecialRequest
	from .root import RootRequest
	from .list import ListRequest
	from .last_modified_by_user import LastModifiedByUserRequest
	from .items import ItemsRequest
	from .following import FollowingRequest
	from .created_by_user import CreatedByUserRequest
	from .bundles import BundlesRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.drive import Drive


class ByDriveIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/drives/{drive%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Drive:
		"""
		Get entity from drives by key
		
		"""
		tags = ['drives.drive']

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
		return await self.request_adapter.send_async(request_info, Drive, error_mapping)

	async def patch(
		self,
		body: Drive,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Drive:
		"""
		Update entity in drives
		
		"""
		tags = ['drives.drive']

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
		return await self.request_adapter.send_async(request_info, Drive, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete entity from drives
		
		"""
		tags = ['drives.drive']
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
	def bundles(self,
	) -> BundlesRequest:
		from .bundles import BundlesRequest
		return BundlesRequest(self.request_adapter, self.path_parameters)

	@property
	def created_by_user(self,
	) -> CreatedByUserRequest:
		from .created_by_user import CreatedByUserRequest
		return CreatedByUserRequest(self.request_adapter, self.path_parameters)

	@property
	def following(self,
	) -> FollowingRequest:
		from .following import FollowingRequest
		return FollowingRequest(self.request_adapter, self.path_parameters)

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
	def list(self,
	) -> ListRequest:
		from .list import ListRequest
		return ListRequest(self.request_adapter, self.path_parameters)

	@property
	def root(self,
	) -> RootRequest:
		from .root import RootRequest
		return RootRequest(self.request_adapter, self.path_parameters)

	@property
	def special(self,
	) -> SpecialRequest:
		from .special import SpecialRequest
		return SpecialRequest(self.request_adapter, self.path_parameters)

