from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class ItemAttachment(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	contentType: Optional[str] = Field(default=None,alias="contentType",)
	isInline: Optional[bool] = Field(default=None,alias="isInline",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	name: Optional[str] = Field(default=None,alias="name",)
	size: Optional[int] = Field(default=None,alias="size",)
	item: Optional[OutlookItem] = Field(default=None,alias="item",)

from .outlook_item import OutlookItem

