from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EventMessageResponseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[EventMessageResponse]] = Field(default=None,alias="value",)

from .event_message_response import EventMessageResponse

