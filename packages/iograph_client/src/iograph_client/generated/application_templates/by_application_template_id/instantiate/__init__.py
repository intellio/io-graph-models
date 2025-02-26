# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.instantiate_post_request import InstantiatePostRequest
from iograph_models.models.application_service_principal import ApplicationServicePrincipal
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class InstantiateRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/applicationTemplates/{applicationTemplate%2Did}/instantiate"
		self.path_parameters: dict[str, Any] = path_parameters

	async def post(
		self,
		body: InstantiatePostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ApplicationServicePrincipal:
		"""
		Invoke action instantiate
		Add an instance of an application from the Microsoft Entra application gallery into your directory. For non-gallery apps, use an application template with one of the following IDs to configure different single sign-on (SSO) modes like SAML SSO and password-based SSO.
		Find more info here: https://learn.microsoft.com/graph/api/applicationtemplate-instantiate?view=graph-rest-1.0
		"""
		tags = ['applicationTemplates.applicationTemplate.Actions']

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
		return await self.request_adapter.send_async(request_info, ApplicationServicePrincipal, error_mapping)


