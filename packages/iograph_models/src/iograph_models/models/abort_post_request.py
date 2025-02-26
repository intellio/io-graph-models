from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AbortPostRequest(BaseModel):
	reason: Optional[str] = Field(default=None,alias="reason",)


