from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuthenticationContextClassReferenceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[AuthenticationContextClassReference]] = Field(default=None,alias="value",)

from .authentication_context_class_reference import AuthenticationContextClassReference

