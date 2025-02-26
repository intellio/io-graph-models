from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudPcManagementGroupAssignmentTarget(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	groupId: Optional[str] = Field(default=None,alias="groupId",)
	servicePlanId: Optional[str] = Field(default=None,alias="servicePlanId",)


