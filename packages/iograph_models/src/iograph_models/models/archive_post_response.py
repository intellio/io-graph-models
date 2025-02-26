from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ArchivePostResponse(BaseModel):
	value: Optional[bool] = Field(default=None,alias="value",)


