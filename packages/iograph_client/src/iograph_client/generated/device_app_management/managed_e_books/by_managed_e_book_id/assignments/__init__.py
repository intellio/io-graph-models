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
	from .by_managed_e_book_assignment_id import ByManagedEBookAssignmentIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.managed_e_book_assignment_collection_response import ManagedEBookAssignmentCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.managed_e_book_assignment import ManagedEBookAssignment


class AssignmentsRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/deviceAppManagement/managedEBooks/{managedEBook%2Did}/assignments"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ManagedEBookAssignmentCollectionResponse:
		"""
		List iosVppEBookAssignments
		List properties and relationships of the iosVppEBookAssignment objects.
		Find more info here: https://learn.microsoft.com/graph/api/intune-books-iosvppebookassignment-list?view=graph-rest-1.0
		"""
		tags = ['deviceAppManagement.managedEBook']

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
		return await self.request_adapter.send_async(request_info, ManagedEBookAssignmentCollectionResponse, error_mapping)

	async def post(
		self,
		body: ManagedEBookAssignment,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ManagedEBookAssignment:
		"""
		Create managedEBookAssignment
		Create a new managedEBookAssignment object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-books-managedebookassignment-create?view=graph-rest-1.0
		"""
		tags = ['deviceAppManagement.managedEBook']

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
		return await self.request_adapter.send_async(request_info, ManagedEBookAssignment, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def by_managed_e_book_assignment_id(self,
		managedEBook_id: str,
		managedEBookAssignment_id: str,
	) -> ByManagedEBookAssignmentIdRequest:
		if managedEBook_id is None:
			raise TypeError("managedEBook_id cannot be null.")
		if managedEBookAssignment_id is None:
			raise TypeError("managedEBookAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedEBook%2Did"] =  managedEBook_id
		path_parameters["managedEBookAssignment%2Did"] =  managedEBookAssignment_id

		from .by_managed_e_book_assignment_id import ByManagedEBookAssignmentIdRequest
		return ByManagedEBookAssignmentIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

