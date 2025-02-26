from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AndroidWorkProfileCompliancePolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[AndroidWorkProfileCompliancePolicy] = Field(alias="value",)

from .android_work_profile_compliance_policy import AndroidWorkProfileCompliancePolicy

