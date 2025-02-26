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
	from .count import CountRequest
	from .by_custom_extension_stage_setting_id import ByCustomExtensionStageSettingIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.custom_extension_stage_setting import CustomExtensionStageSetting
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.custom_extension_stage_setting_collection_response import CustomExtensionStageSettingCollectionResponse


class CustomExtensionStageSettingsRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/identityGovernance/entitlementManagement/assignmentPolicies/{accessPackageAssignmentPolicy%2Did}/customExtensionStageSettings"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> CustomExtensionStageSettingCollectionResponse:
		"""
		Get customExtensionStageSettings from identityGovernance
		The collection of stages when to execute one or more custom access package workflow extensions. Supports $expand.
		"""
		tags = ['identityGovernance.entitlementManagement']

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
		return await self.request_adapter.send_async(request_info, CustomExtensionStageSettingCollectionResponse, error_mapping)

	async def post(
		self,
		body: CustomExtensionStageSetting,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> CustomExtensionStageSetting:
		"""
		Create new navigation property to customExtensionStageSettings for identityGovernance
		
		"""
		tags = ['identityGovernance.entitlementManagement']

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
		return await self.request_adapter.send_async(request_info, CustomExtensionStageSetting, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def by_custom_extension_stage_setting_id(self,
		accessPackageAssignmentPolicy_id: str,
		customExtensionStageSetting_id: str,
	) -> ByCustomExtensionStageSettingIdRequest:
		if accessPackageAssignmentPolicy_id is None:
			raise TypeError("accessPackageAssignmentPolicy_id cannot be null.")
		if customExtensionStageSetting_id is None:
			raise TypeError("customExtensionStageSetting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageAssignmentPolicy%2Did"] =  accessPackageAssignmentPolicy_id
		path_parameters["customExtensionStageSetting%2Did"] =  customExtensionStageSetting_id

		from .by_custom_extension_stage_setting_id import ByCustomExtensionStageSettingIdRequest
		return ByCustomExtensionStageSettingIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

