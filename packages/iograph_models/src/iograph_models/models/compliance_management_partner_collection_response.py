from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ComplianceManagementPartnerCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[ComplianceManagementPartner] = Field(alias="value",)

from .compliance_management_partner import ComplianceManagementPartner

