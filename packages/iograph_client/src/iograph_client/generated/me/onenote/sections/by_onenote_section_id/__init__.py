# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .parent_section_group import ParentSectionGroupRequest
	from .parent_notebook import ParentNotebookRequest
	from .pages import PagesRequest
	from .copy_to_section_group import CopyToSectionGroupRequest
	from .copy_to_notebook import CopyToNotebookRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.onenote_section import OnenoteSection
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByOnenoteSectionIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/me/onenote/sections/{onenoteSection%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> OnenoteSection:
		"""
		Get section
		Retrieve the properties and relationships of a onenoteSection object.
		Find more info here: https://learn.microsoft.com/graph/api/section-get?view=graph-rest-1.0
		"""
		tags = ['me.onenote']

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
		return await self.request_adapter.send_async(request_info, OnenoteSection, error_mapping)

	async def patch(
		self,
		body: OnenoteSection,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> OnenoteSection:
		"""
		Update the navigation property sections in me
		
		"""
		tags = ['me.onenote']

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
		return await self.request_adapter.send_async(request_info, OnenoteSection, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property sections for me
		
		"""
		tags = ['me.onenote']
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
	def copy_to_notebook(self,
	) -> CopyToNotebookRequest:
		from .copy_to_notebook import CopyToNotebookRequest
		return CopyToNotebookRequest(self.request_adapter, self.path_parameters)

	@property
	def copy_to_section_group(self,
	) -> CopyToSectionGroupRequest:
		from .copy_to_section_group import CopyToSectionGroupRequest
		return CopyToSectionGroupRequest(self.request_adapter, self.path_parameters)

	@property
	def pages(self,
	) -> PagesRequest:
		from .pages import PagesRequest
		return PagesRequest(self.request_adapter, self.path_parameters)

	@property
	def parent_notebook(self,
	) -> ParentNotebookRequest:
		from .parent_notebook import ParentNotebookRequest
		return ParentNotebookRequest(self.request_adapter, self.path_parameters)

	@property
	def parent_section_group(self,
	) -> ParentSectionGroupRequest:
		from .parent_section_group import ParentSectionGroupRequest
		return ParentSectionGroupRequest(self.request_adapter, self.path_parameters)

