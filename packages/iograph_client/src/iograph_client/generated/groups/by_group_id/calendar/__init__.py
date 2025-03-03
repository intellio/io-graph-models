# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .get_schedule import GetScheduleRequest
	from .events import EventsRequest
	from .calendar_view import CalendarViewRequest
	from .calendar_permissions import CalendarPermissionsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.calendar import Calendar
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class CalendarRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/calendar", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Calendar:
		"""
		Get calendar from groups
		The group's calendar. Read-only.
		"""
		tags = ['groups.calendar']

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
		return await self.request_adapter.send_async(request_info, Calendar, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> CalendarRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: CalendarRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return CalendarRequest(self.request_adapter, self.path_parameters)

	@property
	def calendar_permissions(self,
	) -> CalendarPermissionsRequest:
		from .calendar_permissions import CalendarPermissionsRequest
		return CalendarPermissionsRequest(self.request_adapter, self.path_parameters)

	@property
	def calendar_view(self,
	) -> CalendarViewRequest:
		from .calendar_view import CalendarViewRequest
		return CalendarViewRequest(self.request_adapter, self.path_parameters)

	@property
	def events(self,
	) -> EventsRequest:
		from .events import EventsRequest
		return EventsRequest(self.request_adapter, self.path_parameters)

	@property
	def get_schedule(self,
	) -> GetScheduleRequest:
		from .get_schedule import GetScheduleRequest
		return GetScheduleRequest(self.request_adapter, self.path_parameters)

