from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OnAuthenticationMethodLoadStartListenerCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[OnAuthenticationMethodLoadStartListener]] = Field(default=None,alias="value",)

from .on_authentication_method_load_start_listener import OnAuthenticationMethodLoadStartListener

