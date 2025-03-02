from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IosHomeScreenApp(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	bundleID: Optional[str] = Field(default=None,alias="bundleID",)


