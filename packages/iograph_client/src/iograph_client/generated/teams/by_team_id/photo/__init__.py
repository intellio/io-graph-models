# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .value import ValueRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.profile_photo import ProfilePhoto


class PhotoRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/teams/{team%2Did}/photo"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ProfilePhoto:
		"""
		Get profilePhoto
		Get the specified profilePhoto or its metadata (profilePhoto properties). The supported sizes of HD photos on Microsoft 365 are as follows: 48x48, 64x64, 96x96, 120x120, 240x240,
360x360, 432x432, 504x504, and 648x648. Photos can be any dimension if they're stored in Microsoft Entra ID. You can get the metadata of the largest available photo or specify a size to get the metadata for that photo size.
If the size you request is unavailable, you can still get a smaller size that the user has uploaded and made available.
For example, if the user uploads a photo that is 504x504 pixels, all but the 648x648 size of the photo is available for download.
		Find more info here: https://learn.microsoft.com/graph/api/profilephoto-get?view=graph-rest-1.0
		"""
		tags = ['teams.profilePhoto']

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
		return await self.request_adapter.send_async(request_info, ProfilePhoto, error_mapping)

	async def patch(
		self,
		body: ProfilePhoto,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ProfilePhoto:
		"""
		Update profilePhoto
		Update the photo for the specified contact, group, team, or user in a tenant. The size of the photo you can update to is limited to 4 MB. You can use either PATCH or PUT for this operation.
		Find more info here: https://learn.microsoft.com/graph/api/profilephoto-update?view=graph-rest-1.0
		"""
		tags = ['teams.profilePhoto']

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
		return await self.request_adapter.send_async(request_info, ProfilePhoto, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	@property
	def value(self,
	) -> ValueRequest:
		from .value import ValueRequest
		return ValueRequest(self.request_adapter, self.path_parameters)

