from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TargetManager(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	managerLevel: Optional[int] = Field(default=None,alias="managerLevel",)


