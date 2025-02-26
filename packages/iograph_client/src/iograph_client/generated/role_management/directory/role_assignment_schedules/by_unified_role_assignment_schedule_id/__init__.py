# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .role_definition import RoleDefinitionRequest
	from .principal import PrincipalRequest
	from .directory_scope import DirectoryScopeRequest
	from .app_scope import AppScopeRequest
	from .activated_using import ActivatedUsingRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.unified_role_assignment_schedule import UnifiedRoleAssignmentSchedule


class ByUnifiedRoleAssignmentScheduleIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/roleManagement/directory/roleAssignmentSchedules/{unifiedRoleAssignmentSchedule%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> UnifiedRoleAssignmentSchedule:
		"""
		Get unifiedRoleAssignmentSchedule
		Retrieve the schedule for an active role assignment operation.
		Find more info here: https://learn.microsoft.com/graph/api/unifiedroleassignmentschedule-get?view=graph-rest-1.0
		"""
		tags = ['roleManagement.rbacApplication']

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
		return await self.request_adapter.send_async(request_info, UnifiedRoleAssignmentSchedule, error_mapping)

	async def patch(
		self,
		body: UnifiedRoleAssignmentSchedule,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UnifiedRoleAssignmentSchedule:
		"""
		Update the navigation property roleAssignmentSchedules in roleManagement
		
		"""
		tags = ['roleManagement.rbacApplication']

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
		return await self.request_adapter.send_async(request_info, UnifiedRoleAssignmentSchedule, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property roleAssignmentSchedules for roleManagement
		
		"""
		tags = ['roleManagement.rbacApplication']
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
	def activated_using(self,
	) -> ActivatedUsingRequest:
		from .activated_using import ActivatedUsingRequest
		return ActivatedUsingRequest(self.request_adapter, self.path_parameters)

	@property
	def app_scope(self,
	) -> AppScopeRequest:
		from .app_scope import AppScopeRequest
		return AppScopeRequest(self.request_adapter, self.path_parameters)

	@property
	def directory_scope(self,
	) -> DirectoryScopeRequest:
		from .directory_scope import DirectoryScopeRequest
		return DirectoryScopeRequest(self.request_adapter, self.path_parameters)

	@property
	def principal(self,
	) -> PrincipalRequest:
		from .principal import PrincipalRequest
		return PrincipalRequest(self.request_adapter, self.path_parameters)

	@property
	def role_definition(self,
	) -> RoleDefinitionRequest:
		from .role_definition import RoleDefinitionRequest
		return RoleDefinitionRequest(self.request_adapter, self.path_parameters)

