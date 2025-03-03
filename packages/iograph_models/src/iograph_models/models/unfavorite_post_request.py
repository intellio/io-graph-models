from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UnfavoritePostRequest(BaseModel):
	messageIds: Optional[list[str]] = Field(default=None,alias="messageIds",)


