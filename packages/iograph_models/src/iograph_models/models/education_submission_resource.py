from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EducationSubmissionResource(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	assignmentResourceUrl: Optional[str] = Field(default=None,alias="assignmentResourceUrl",)
	resource: Optional[EducationResource] = Field(default=None,alias="resource",)

from .education_resource import EducationResource

