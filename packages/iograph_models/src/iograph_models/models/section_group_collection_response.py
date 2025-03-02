from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SectionGroupCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[SectionGroup]] = Field(default=None,alias="value",)

from .section_group import SectionGroup

