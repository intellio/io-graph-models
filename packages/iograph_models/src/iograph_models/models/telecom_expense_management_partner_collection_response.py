from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TelecomExpenseManagementPartnerCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[TelecomExpenseManagementPartner]] = Field(default=None,alias="value",)

from .telecom_expense_management_partner import TelecomExpenseManagementPartner

