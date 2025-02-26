from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AndroidCompliancePolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[AndroidCompliancePolicy] = Field(alias="value",)

from .android_compliance_policy import AndroidCompliancePolicy

