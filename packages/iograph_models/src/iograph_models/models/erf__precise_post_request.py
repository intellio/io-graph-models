from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Erf__precisePostRequest(BaseModel):
	X: Optional[str] = Field(default=None,alias="X",)


