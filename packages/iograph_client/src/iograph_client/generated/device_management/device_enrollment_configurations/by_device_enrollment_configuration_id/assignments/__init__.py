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
	from .by_enrollment_configuration_assignment_id import ByEnrollmentConfigurationAssignmentIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.enrollment_configuration_assignment import EnrollmentConfigurationAssignment
from iograph_models.models.enrollment_configuration_assignment_collection_response import EnrollmentConfigurationAssignmentCollectionResponse


class AssignmentsRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/deviceManagement/deviceEnrollmentConfigurations/{deviceEnrollmentConfiguration%2Did}/assignments"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EnrollmentConfigurationAssignmentCollectionResponse:
		"""
		List enrollmentConfigurationAssignments
		List properties and relationships of the enrollmentConfigurationAssignment objects.
		Find more info here: https://learn.microsoft.com/graph/api/intune-onboarding-enrollmentconfigurationassignment-list?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.deviceEnrollmentConfiguration']

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
		return await self.request_adapter.send_async(request_info, EnrollmentConfigurationAssignmentCollectionResponse, error_mapping)

	async def post(
		self,
		body: EnrollmentConfigurationAssignment,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EnrollmentConfigurationAssignment:
		"""
		Create enrollmentConfigurationAssignment
		Create a new enrollmentConfigurationAssignment object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-onboarding-enrollmentconfigurationassignment-create?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.deviceEnrollmentConfiguration']

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
		return await self.request_adapter.send_async(request_info, EnrollmentConfigurationAssignment, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def by_enrollment_configuration_assignment_id(self,
		deviceEnrollmentConfiguration_id: str,
		enrollmentConfigurationAssignment_id: str,
	) -> ByEnrollmentConfigurationAssignmentIdRequest:
		if deviceEnrollmentConfiguration_id is None:
			raise TypeError("deviceEnrollmentConfiguration_id cannot be null.")
		if enrollmentConfigurationAssignment_id is None:
			raise TypeError("enrollmentConfigurationAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceEnrollmentConfiguration%2Did"] =  deviceEnrollmentConfiguration_id
		path_parameters["enrollmentConfigurationAssignment%2Did"] =  enrollmentConfigurationAssignment_id

		from .by_enrollment_configuration_assignment_id import ByEnrollmentConfigurationAssignmentIdRequest
		return ByEnrollmentConfigurationAssignmentIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

