from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CertificateBasedAuthConfiguration(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	certificateAuthorities: list[CertificateAuthority] = Field(alias="certificateAuthorities",)

from .certificate_authority import CertificateAuthority

