from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class LearningSelfInitiatedCourseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[LearningSelfInitiatedCourse]] = Field(default=None,alias="value",)

from .learning_self_initiated_course import LearningSelfInitiatedCourse

