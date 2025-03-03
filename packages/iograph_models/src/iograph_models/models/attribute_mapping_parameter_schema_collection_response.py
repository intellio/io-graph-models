from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AttributeMappingParameterSchemaCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[AttributeMappingParameterSchema]] = Field(default=None,alias="value",)

from .attribute_mapping_parameter_schema import AttributeMappingParameterSchema

