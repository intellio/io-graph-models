from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityFileEvidenceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[SecurityFileEvidence]] = Field(default=None,alias="value",)

from .security_file_evidence import SecurityFileEvidence

