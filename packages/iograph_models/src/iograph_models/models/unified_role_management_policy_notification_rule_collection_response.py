from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UnifiedRoleManagementPolicyNotificationRuleCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[UnifiedRoleManagementPolicyNotificationRule]] = Field(default=None,alias="value",)

from .unified_role_management_policy_notification_rule import UnifiedRoleManagementPolicyNotificationRule

