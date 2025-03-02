from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DomainDnsSrvRecordCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[DomainDnsSrvRecord]] = Field(default=None,alias="value",)

from .domain_dns_srv_record import DomainDnsSrvRecord

