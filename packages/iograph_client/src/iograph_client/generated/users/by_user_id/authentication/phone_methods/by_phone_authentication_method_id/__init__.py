# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .enable_sms_sign_in import EnableSmsSignInRequest
	from .disable_sms_sign_in import DisableSmsSignInRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.phone_authentication_method import PhoneAuthenticationMethod
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByPhoneAuthenticationMethodIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/users/{user%2Did}/authentication/phoneMethods/{phoneAuthenticationMethod%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PhoneAuthenticationMethod:
		"""
		Get phoneMethods from users
		The phone numbers registered to a user for authentication.
		"""
		tags = ['users.authentication']

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
		return await self.request_adapter.send_async(request_info, PhoneAuthenticationMethod, error_mapping)

	async def patch(
		self,
		body: PhoneAuthenticationMethod,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PhoneAuthenticationMethod:
		"""
		Update phoneAuthenticationMethod
		Update a user's phone number associated with a phone authentication method object. You can't change a phone's type. To change a phone's type, add a new number of the desired type and then delete the object with the original type. If a user is enabled by policy to use SMS to sign in and the mobile number is changed, the system will attempt to register the number for use in that system. Self-service operations aren't supported.
		Find more info here: https://learn.microsoft.com/graph/api/phoneauthenticationmethod-update?view=graph-rest-1.0
		"""
		tags = ['users.authentication']

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
		return await self.request_adapter.send_async(request_info, PhoneAuthenticationMethod, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property phoneMethods for users
		
		"""
		tags = ['users.authentication']
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
	def disable_sms_sign_in(self,
	) -> DisableSmsSignInRequest:
		from .disable_sms_sign_in import DisableSmsSignInRequest
		return DisableSmsSignInRequest(self.request_adapter, self.path_parameters)

	@property
	def enable_sms_sign_in(self,
	) -> EnableSmsSignInRequest:
		from .enable_sms_sign_in import EnableSmsSignInRequest
		return EnableSmsSignInRequest(self.request_adapter, self.path_parameters)

