from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SoftwareOathAuthenticationMethodConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[SoftwareOathAuthenticationMethodConfiguration]] = Field(default=None,alias="value",)

from .software_oath_authentication_method_configuration import SoftwareOathAuthenticationMethodConfiguration

