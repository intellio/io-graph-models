from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_by_idsPostRequest(BaseModel):
	ids: Optional[list[str]] = Field(default=None,alias="ids",)
	types: Optional[list[str]] = Field(default=None,alias="types",)


