from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MicrosoftAuthenticatorAuthenticationMethodConfiguration(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	excludeTargets: Optional[list[ExcludeTarget]] = Field(default=None,alias="excludeTargets",)
	state: Optional[AuthenticationMethodState] = Field(default=None,alias="state",)
	featureSettings: Optional[MicrosoftAuthenticatorFeatureSettings] = Field(default=None,alias="featureSettings",)
	isSoftwareOathEnabled: Optional[bool] = Field(default=None,alias="isSoftwareOathEnabled",)
	includeTargets: Optional[list[MicrosoftAuthenticatorAuthenticationMethodTarget]] = Field(default=None,alias="includeTargets",)

from .exclude_target import ExcludeTarget
from .authentication_method_state import AuthenticationMethodState
from .microsoft_authenticator_feature_settings import MicrosoftAuthenticatorFeatureSettings
from .microsoft_authenticator_authentication_method_target import MicrosoftAuthenticatorAuthenticationMethodTarget

