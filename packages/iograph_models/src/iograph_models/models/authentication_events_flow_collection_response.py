from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuthenticationEventsFlowCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[AuthenticationEventsFlow] = Field(alias="value",)

from .authentication_events_flow import AuthenticationEventsFlow

