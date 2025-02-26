from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class BrowserSiteCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[BrowserSite] = Field(alias="value",)

from .browser_site import BrowserSite

