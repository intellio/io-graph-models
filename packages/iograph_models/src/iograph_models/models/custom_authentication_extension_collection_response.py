from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CustomAuthenticationExtensionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[CustomAuthenticationExtension]] = Field(default=None,alias="value",)

from .custom_authentication_extension import CustomAuthenticationExtension

