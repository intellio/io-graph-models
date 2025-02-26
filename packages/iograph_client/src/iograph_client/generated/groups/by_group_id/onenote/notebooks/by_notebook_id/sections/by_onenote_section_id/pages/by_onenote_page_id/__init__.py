# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .parent_section import ParentSectionRequest
	from .parent_notebook import ParentNotebookRequest
	from .onenote_patch_content import OnenotePatchContentRequest
	from .copy_to_section import CopyToSectionRequest
	from .content import ContentRequest
	from ...........request_adapter import HttpxRequestAdapter
from iograph_models.models.onenote_page import OnenotePage
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByOnenotePageIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/groups/{group%2Did}/onenote/notebooks/{notebook%2Did}/sections/{onenoteSection%2Did}/pages/{onenotePage%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> OnenotePage:
		"""
		Get pages from groups
		The collection of pages in the section.  Read-only. Nullable.
		"""
		tags = ['groups.onenote']

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
		return await self.request_adapter.send_async(request_info, OnenotePage, error_mapping)

	async def patch(
		self,
		body: OnenotePage,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> OnenotePage:
		"""
		Update the navigation property pages in groups
		
		"""
		tags = ['groups.onenote']

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
		return await self.request_adapter.send_async(request_info, OnenotePage, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property pages for groups
		
		"""
		tags = ['groups.onenote']
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
	def content(self,
	) -> ContentRequest:
		from .content import ContentRequest
		return ContentRequest(self.request_adapter, self.path_parameters)

	@property
	def copy_to_section(self,
	) -> CopyToSectionRequest:
		from .copy_to_section import CopyToSectionRequest
		return CopyToSectionRequest(self.request_adapter, self.path_parameters)

	@property
	def onenote_patch_content(self,
	) -> OnenotePatchContentRequest:
		from .onenote_patch_content import OnenotePatchContentRequest
		return OnenotePatchContentRequest(self.request_adapter, self.path_parameters)

	@property
	def parent_notebook(self,
	) -> ParentNotebookRequest:
		from .parent_notebook import ParentNotebookRequest
		return ParentNotebookRequest(self.request_adapter, self.path_parameters)

	@property
	def parent_section(self,
	) -> ParentSectionRequest:
		from .parent_section import ParentSectionRequest
		return ParentSectionRequest(self.request_adapter, self.path_parameters)

