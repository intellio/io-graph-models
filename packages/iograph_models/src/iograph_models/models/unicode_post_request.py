from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UnicodePostRequest(BaseModel):
	text: Optional[str] = Field(default=None,alias="text",)


