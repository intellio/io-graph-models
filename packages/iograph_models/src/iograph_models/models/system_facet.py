from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SystemFacet(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


