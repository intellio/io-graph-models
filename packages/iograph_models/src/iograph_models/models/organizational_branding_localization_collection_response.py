from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OrganizationalBrandingLocalizationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[OrganizationalBrandingLocalization]] = Field(default=None,alias="value",)

from .organizational_branding_localization import OrganizationalBrandingLocalization

