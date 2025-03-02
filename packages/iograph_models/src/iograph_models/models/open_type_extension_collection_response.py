from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OpenTypeExtensionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[OpenTypeExtension]] = Field(default=None,alias="value",)

from .open_type_extension import OpenTypeExtension

