# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .submissions import SubmissionsRequest
	from .rubric import RubricRequest
	from .resources import ResourcesRequest
	from .set_up_resources_folder import SetUpResourcesFolderRequest
	from .set_up_feedback_resources_folder import SetUpFeedbackResourcesFolderRequest
	from .publish import PublishRequest
	from .deactivate import DeactivateRequest
	from .activate import ActivateRequest
	from .grading_category import GradingCategoryRequest
	from .categories import CategoriesRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.education_assignment import EducationAssignment


class ByEducationAssignmentIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/education/users/{educationUser%2Did}/assignments/{educationAssignment%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EducationAssignment:
		"""
		Get assignments from education
		Assignments belonging to the user.
		"""
		tags = ['education.educationUser']

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
		return await self.request_adapter.send_async(request_info, EducationAssignment, error_mapping)

	async def patch(
		self,
		body: EducationAssignment,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EducationAssignment:
		"""
		Update the navigation property assignments in education
		
		"""
		tags = ['education.educationUser']

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
		return await self.request_adapter.send_async(request_info, EducationAssignment, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property assignments for education
		
		"""
		tags = ['education.educationUser']
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
	def categories(self,
	) -> CategoriesRequest:
		from .categories import CategoriesRequest
		return CategoriesRequest(self.request_adapter, self.path_parameters)

	@property
	def grading_category(self,
	) -> GradingCategoryRequest:
		from .grading_category import GradingCategoryRequest
		return GradingCategoryRequest(self.request_adapter, self.path_parameters)

	@property
	def activate(self,
	) -> ActivateRequest:
		from .activate import ActivateRequest
		return ActivateRequest(self.request_adapter, self.path_parameters)

	@property
	def deactivate(self,
	) -> DeactivateRequest:
		from .deactivate import DeactivateRequest
		return DeactivateRequest(self.request_adapter, self.path_parameters)

	@property
	def publish(self,
	) -> PublishRequest:
		from .publish import PublishRequest
		return PublishRequest(self.request_adapter, self.path_parameters)

	@property
	def set_up_feedback_resources_folder(self,
	) -> SetUpFeedbackResourcesFolderRequest:
		from .set_up_feedback_resources_folder import SetUpFeedbackResourcesFolderRequest
		return SetUpFeedbackResourcesFolderRequest(self.request_adapter, self.path_parameters)

	@property
	def set_up_resources_folder(self,
	) -> SetUpResourcesFolderRequest:
		from .set_up_resources_folder import SetUpResourcesFolderRequest
		return SetUpResourcesFolderRequest(self.request_adapter, self.path_parameters)

	@property
	def resources(self,
	) -> ResourcesRequest:
		from .resources import ResourcesRequest
		return ResourcesRequest(self.request_adapter, self.path_parameters)

	@property
	def rubric(self,
	) -> RubricRequest:
		from .rubric import RubricRequest
		return RubricRequest(self.request_adapter, self.path_parameters)

	@property
	def submissions(self,
	) -> SubmissionsRequest:
		from .submissions import SubmissionsRequest
		return SubmissionsRequest(self.request_adapter, self.path_parameters)

