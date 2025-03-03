from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ManagedDeviceMobileAppConfigurationUserStatusCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[ManagedDeviceMobileAppConfigurationUserStatus]] = Field(default=None,alias="value",)

from .managed_device_mobile_app_configuration_user_status import ManagedDeviceMobileAppConfigurationUserStatus

