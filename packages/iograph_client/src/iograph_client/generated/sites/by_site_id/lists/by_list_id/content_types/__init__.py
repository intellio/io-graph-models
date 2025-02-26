# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .add_copy_from_content_type_hub import AddCopyFromContentTypeHubRequest
	from .add_copy import AddCopyRequest
	from .count import CountRequest
	from .by_content_type_id import ByContentTypeIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.content_type_collection_response import ContentTypeCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.content_type import ContentType


class ContentTypesRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/sites/{site%2Did}/lists/{list%2Did}/contentTypes"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ContentTypeCollectionResponse:
		"""
		List contentTypes in a list
		Get the collection of contentType resources in a list.
		Find more info here: https://learn.microsoft.com/graph/api/list-list-contenttypes?view=graph-rest-1.0
		"""
		tags = ['sites.list']

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
		return await self.request_adapter.send_async(request_info, ContentTypeCollectionResponse, error_mapping)

	async def post(
		self,
		body: ContentType,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ContentType:
		"""
		Create new navigation property to contentTypes for sites
		
		"""
		tags = ['sites.list']

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
		return await self.request_adapter.send_async(request_info, ContentType, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def by_content_type_id(self,
		site_id: str,
		list_id: str,
		contentType_id: str,
	) -> ByContentTypeIdRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if list_id is None:
			raise TypeError("list_id cannot be null.")
		if contentType_id is None:
			raise TypeError("contentType_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["list%2Did"] =  list_id
		path_parameters["contentType%2Did"] =  contentType_id

		from .by_content_type_id import ByContentTypeIdRequest
		return ByContentTypeIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def add_copy(self,
	) -> AddCopyRequest:
		from .add_copy import AddCopyRequest
		return AddCopyRequest(self.request_adapter, self.path_parameters)

	@property
	def add_copy_from_content_type_hub(self,
	) -> AddCopyFromContentTypeHubRequest:
		from .add_copy_from_content_type_hub import AddCopyFromContentTypeHubRequest
		return AddCopyFromContentTypeHubRequest(self.request_adapter, self.path_parameters)

