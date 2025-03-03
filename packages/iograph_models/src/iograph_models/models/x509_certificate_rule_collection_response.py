from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class X509CertificateRuleCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[X509CertificateRule]] = Field(default=None,alias="value",)

from .x509_certificate_rule import X509CertificateRule

