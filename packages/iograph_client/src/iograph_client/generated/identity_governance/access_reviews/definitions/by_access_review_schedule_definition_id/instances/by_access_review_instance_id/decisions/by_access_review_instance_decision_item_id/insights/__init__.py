# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_governance_insight_id import ByGovernanceInsightIdRequest
	from ...........request_adapter import HttpxRequestAdapter
from iograph_models.models.governance_insight import GovernanceInsight
from iograph_models.models.governance_insight_collection_response import GovernanceInsightCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class InsightsRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/identityGovernance/accessReviews/definitions/{accessReviewScheduleDefinition%2Did}/instances/{accessReviewInstance%2Did}/decisions/{accessReviewInstanceDecisionItem%2Did}/insights"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> GovernanceInsightCollectionResponse:
		"""
		Get insights from identityGovernance
		Insights are recommendations to reviewers on whether to approve or deny a decision. There can be multiple insights associated with an accessReviewInstanceDecisionItem.
		"""
		tags = ['identityGovernance.accessReviewSet']

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
		return await self.request_adapter.send_async(request_info, GovernanceInsightCollectionResponse, error_mapping)

	async def post(
		self,
		body: GovernanceInsight,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> GovernanceInsight:
		"""
		Create new navigation property to insights for identityGovernance
		
		"""
		tags = ['identityGovernance.accessReviewSet']

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
		return await self.request_adapter.send_async(request_info, GovernanceInsight, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def by_governance_insight_id(self,
		accessReviewScheduleDefinition_id: str,
		accessReviewInstance_id: str,
		accessReviewInstanceDecisionItem_id: str,
		governanceInsight_id: str,
	) -> ByGovernanceInsightIdRequest:
		if accessReviewScheduleDefinition_id is None:
			raise TypeError("accessReviewScheduleDefinition_id cannot be null.")
		if accessReviewInstance_id is None:
			raise TypeError("accessReviewInstance_id cannot be null.")
		if accessReviewInstanceDecisionItem_id is None:
			raise TypeError("accessReviewInstanceDecisionItem_id cannot be null.")
		if governanceInsight_id is None:
			raise TypeError("governanceInsight_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessReviewScheduleDefinition%2Did"] =  accessReviewScheduleDefinition_id
		path_parameters["accessReviewInstance%2Did"] =  accessReviewInstance_id
		path_parameters["accessReviewInstanceDecisionItem%2Did"] =  accessReviewInstanceDecisionItem_id
		path_parameters["governanceInsight%2Did"] =  governanceInsight_id

		from .by_governance_insight_id import ByGovernanceInsightIdRequest
		return ByGovernanceInsightIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

