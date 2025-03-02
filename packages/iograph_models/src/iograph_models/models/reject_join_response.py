from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RejectJoinResponse(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	reason: Optional[RejectReason] = Field(default=None,alias="reason",)

from .reject_reason import RejectReason

