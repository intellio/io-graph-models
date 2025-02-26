# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_print_task_id import ByPrintTaskIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.print_task_collection_response import PrintTaskCollectionResponse
from iograph_models.models.print_task import PrintTask


class TasksRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/print/taskDefinitions/{printTaskDefinition%2Did}/tasks"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PrintTaskCollectionResponse:
		"""
		List tasks
		Retrieve a list of tasks associated with a task definition. For details about how to use this API to add pull printing support to Universal Print, see Extending Universal Print to support pull printing.
		Find more info here: https://learn.microsoft.com/graph/api/printtaskdefinition-list-tasks?view=graph-rest-1.0
		"""
		tags = ['print.printTaskDefinition']

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
		return await self.request_adapter.send_async(request_info, PrintTaskCollectionResponse, error_mapping)

	async def post(
		self,
		body: PrintTask,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PrintTask:
		"""
		Create new navigation property to tasks for print
		
		"""
		tags = ['print.printTaskDefinition']

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
		return await self.request_adapter.send_async(request_info, PrintTask, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def by_print_task_id(self,
		printTaskDefinition_id: str,
		printTask_id: str,
	) -> ByPrintTaskIdRequest:
		if printTaskDefinition_id is None:
			raise TypeError("printTaskDefinition_id cannot be null.")
		if printTask_id is None:
			raise TypeError("printTask_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["printTaskDefinition%2Did"] =  printTaskDefinition_id
		path_parameters["printTask%2Did"] =  printTask_id

		from .by_print_task_id import ByPrintTaskIdRequest
		return ByPrintTaskIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

