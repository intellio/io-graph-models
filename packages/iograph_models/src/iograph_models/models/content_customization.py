from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ContentCustomization(BaseModel):
	attributeCollection: list[KeyValue] = Field(alias="attributeCollection",)
	attributeCollectionRelativeUrl: Optional[str] = Field(default=None,alias="attributeCollectionRelativeUrl",)
	registrationCampaign: list[KeyValue] = Field(alias="registrationCampaign",)
	registrationCampaignRelativeUrl: Optional[str] = Field(default=None,alias="registrationCampaignRelativeUrl",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .key_value import KeyValue
from .key_value import KeyValue

