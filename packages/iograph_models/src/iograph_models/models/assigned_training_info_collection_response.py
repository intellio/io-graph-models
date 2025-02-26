from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AssignedTrainingInfoCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[AssignedTrainingInfo] = Field(alias="value",)

from .assigned_training_info import AssignedTrainingInfo

