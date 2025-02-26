# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .tables import TablesRequest
	from .protection import ProtectionRequest
	from .pivot_tables import PivotTablesRequest
	from .names import NamesRequest
	from .charts import ChartsRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.workbook_worksheet import WorkbookWorksheet


class ByWorkbookWorksheetIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/worksheets/{workbookWorksheet%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> WorkbookWorksheet:
		"""
		Get worksheets from drives
		Represents a collection of worksheets associated with the workbook. Read-only.
		"""
		tags = ['drives.driveItem']

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
		return await self.request_adapter.send_async(request_info, WorkbookWorksheet, error_mapping)

	async def patch(
		self,
		body: WorkbookWorksheet,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WorkbookWorksheet:
		"""
		Update the navigation property worksheets in drives
		
		"""
		tags = ['drives.driveItem']

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
		return await self.request_adapter.send_async(request_info, WorkbookWorksheet, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property worksheets for drives
		
		"""
		tags = ['drives.driveItem']
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
	def charts(self,
	) -> ChartsRequest:
		from .charts import ChartsRequest
		return ChartsRequest(self.request_adapter, self.path_parameters)

	@property
	def names(self,
	) -> NamesRequest:
		from .names import NamesRequest
		return NamesRequest(self.request_adapter, self.path_parameters)

	@property
	def pivot_tables(self,
	) -> PivotTablesRequest:
		from .pivot_tables import PivotTablesRequest
		return PivotTablesRequest(self.request_adapter, self.path_parameters)

	@property
	def protection(self,
	) -> ProtectionRequest:
		from .protection import ProtectionRequest
		return ProtectionRequest(self.request_adapter, self.path_parameters)

	@property
	def tables(self,
	) -> TablesRequest:
		from .tables import TablesRequest
		return TablesRequest(self.request_adapter, self.path_parameters)

