from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuditPropertyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[AuditProperty] = Field(alias="value",)

from .audit_property import AuditProperty

