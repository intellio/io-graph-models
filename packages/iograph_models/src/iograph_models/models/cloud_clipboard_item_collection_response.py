from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudClipboardItemCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[CloudClipboardItem]] = Field(default=None,alias="value",)

from .cloud_clipboard_item import CloudClipboardItem

