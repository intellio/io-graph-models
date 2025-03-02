from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserFlowLanguageConfiguration(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	isEnabled: Optional[bool] = Field(default=None,alias="isEnabled",)
	defaultPages: Optional[list[UserFlowLanguagePage]] = Field(default=None,alias="defaultPages",)
	overridesPages: Optional[list[UserFlowLanguagePage]] = Field(default=None,alias="overridesPages",)

from .user_flow_language_page import UserFlowLanguagePage
from .user_flow_language_page import UserFlowLanguagePage

