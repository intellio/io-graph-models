from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CalculatePostRequest(BaseModel):
	calculationType: Optional[str] = Field(default=None,alias="calculationType",)


