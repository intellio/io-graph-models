from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DefaultColumnValue(BaseModel):
	formula: Optional[str] = Field(default=None,alias="formula",)
	value: Optional[str] = Field(default=None,alias="value",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


