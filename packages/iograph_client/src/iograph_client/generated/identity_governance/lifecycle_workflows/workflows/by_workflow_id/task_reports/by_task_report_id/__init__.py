# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .task_processing_results import TaskProcessingResultsRequest
	from .task_definition import TaskDefinitionRequest
	from .task import TaskRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.models.identity_governance_task_report import IdentityGovernanceTaskReport
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByTaskReportIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/identityGovernance/lifecycleWorkflows/workflows/{workflow%2Did}/taskReports/{taskReport%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> IdentityGovernanceTaskReport:
		"""
		Get taskReports from identityGovernance
		Represents the aggregation of task execution data for tasks within a workflow object.
		"""
		tags = ['identityGovernance.lifecycleWorkflowsContainer']

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
		return await self.request_adapter.send_async(request_info, IdentityGovernanceTaskReport, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	@property
	def task(self,
	) -> TaskRequest:
		from .task import TaskRequest
		return TaskRequest(self.request_adapter, self.path_parameters)

	@property
	def task_definition(self,
	) -> TaskDefinitionRequest:
		from .task_definition import TaskDefinitionRequest
		return TaskDefinitionRequest(self.request_adapter, self.path_parameters)

	@property
	def task_processing_results(self,
	) -> TaskProcessingResultsRequest:
		from .task_processing_results import TaskProcessingResultsRequest
		return TaskProcessingResultsRequest(self.request_adapter, self.path_parameters)

