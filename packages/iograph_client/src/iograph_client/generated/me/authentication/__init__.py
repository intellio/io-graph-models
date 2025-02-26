# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .windows_hello_for_business_methods import WindowsHelloForBusinessMethodsRequest
	from .temporary_access_pass_methods import TemporaryAccessPassMethodsRequest
	from .software_oath_methods import SoftwareOathMethodsRequest
	from .phone_methods import PhoneMethodsRequest
	from .password_methods import PasswordMethodsRequest
	from .operations import OperationsRequest
	from .microsoft_authenticator_methods import MicrosoftAuthenticatorMethodsRequest
	from .methods import MethodsRequest
	from .fido2_methods import Fido2MethodsRequest
	from .email_methods import EmailMethodsRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.authentication import Authentication


class AuthenticationRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/me/authentication"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Authentication:
		"""
		Get authentication from me
		The authentication methods that are supported for the user.
		"""
		tags = ['me.authentication']

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
		return await self.request_adapter.send_async(request_info, Authentication, error_mapping)

	async def patch(
		self,
		body: Authentication,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Authentication:
		"""
		Update the navigation property authentication in me
		
		"""
		tags = ['me.authentication']

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
		return await self.request_adapter.send_async(request_info, Authentication, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property authentication for me
		
		"""
		tags = ['me.authentication']
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
	def email_methods(self,
	) -> EmailMethodsRequest:
		from .email_methods import EmailMethodsRequest
		return EmailMethodsRequest(self.request_adapter, self.path_parameters)

	@property
	def fido2_methods(self,
	) -> Fido2MethodsRequest:
		from .fido2_methods import Fido2MethodsRequest
		return Fido2MethodsRequest(self.request_adapter, self.path_parameters)

	@property
	def methods(self,
	) -> MethodsRequest:
		from .methods import MethodsRequest
		return MethodsRequest(self.request_adapter, self.path_parameters)

	@property
	def microsoft_authenticator_methods(self,
	) -> MicrosoftAuthenticatorMethodsRequest:
		from .microsoft_authenticator_methods import MicrosoftAuthenticatorMethodsRequest
		return MicrosoftAuthenticatorMethodsRequest(self.request_adapter, self.path_parameters)

	@property
	def operations(self,
	) -> OperationsRequest:
		from .operations import OperationsRequest
		return OperationsRequest(self.request_adapter, self.path_parameters)

	@property
	def password_methods(self,
	) -> PasswordMethodsRequest:
		from .password_methods import PasswordMethodsRequest
		return PasswordMethodsRequest(self.request_adapter, self.path_parameters)

	@property
	def phone_methods(self,
	) -> PhoneMethodsRequest:
		from .phone_methods import PhoneMethodsRequest
		return PhoneMethodsRequest(self.request_adapter, self.path_parameters)

	@property
	def software_oath_methods(self,
	) -> SoftwareOathMethodsRequest:
		from .software_oath_methods import SoftwareOathMethodsRequest
		return SoftwareOathMethodsRequest(self.request_adapter, self.path_parameters)

	@property
	def temporary_access_pass_methods(self,
	) -> TemporaryAccessPassMethodsRequest:
		from .temporary_access_pass_methods import TemporaryAccessPassMethodsRequest
		return TemporaryAccessPassMethodsRequest(self.request_adapter, self.path_parameters)

	@property
	def windows_hello_for_business_methods(self,
	) -> WindowsHelloForBusinessMethodsRequest:
		from .windows_hello_for_business_methods import WindowsHelloForBusinessMethodsRequest
		return WindowsHelloForBusinessMethodsRequest(self.request_adapter, self.path_parameters)

