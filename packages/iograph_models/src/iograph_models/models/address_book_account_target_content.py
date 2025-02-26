from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AddressBookAccountTargetContent(BaseModel):
	type: Optional[AccountTargetContentType] = Field(default=None,alias="type",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	accountTargetEmails: list[Optional[str]] = Field(alias="accountTargetEmails",)

from .account_target_content_type import AccountTargetContentType

