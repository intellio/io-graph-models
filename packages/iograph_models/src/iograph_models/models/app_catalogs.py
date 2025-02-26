from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AppCatalogs(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	teamsApps: list[TeamsApp] = Field(alias="teamsApps",)

from .teams_app import TeamsApp

