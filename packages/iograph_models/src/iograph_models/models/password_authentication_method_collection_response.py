from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PasswordAuthenticationMethodCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[PasswordAuthenticationMethod]] = Field(default=None,alias="value",)

from .password_authentication_method import PasswordAuthenticationMethod

