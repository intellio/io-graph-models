from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Chi_sq__invPostRequest(BaseModel):
	probability: Optional[str] = Field(default=None,alias="probability",)
	degFreedom: Optional[str] = Field(default=None,alias="degFreedom",)


