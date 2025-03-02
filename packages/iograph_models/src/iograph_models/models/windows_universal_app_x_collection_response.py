from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsUniversalAppXCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[WindowsUniversalAppX]] = Field(default=None,alias="value",)

from .windows_universal_app_x import WindowsUniversalAppX

