from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ConditionalAccessClientApplications(BaseModel):
	excludeServicePrincipals: list[str] = Field(alias="excludeServicePrincipals",)
	includeServicePrincipals: list[str] = Field(alias="includeServicePrincipals",)
	servicePrincipalFilter: Optional[ConditionalAccessFilter] = Field(default=None,alias="servicePrincipalFilter",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .conditional_access_filter import ConditionalAccessFilter

