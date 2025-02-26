from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Count_ifPostRequest(BaseModel):
	range: Optional[str] = Field(default=None,alias="range",)
	criteria: Optional[str] = Field(default=None,alias="criteria",)


