from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WorkbookChartGridlinesFormat(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	line: Optional[WorkbookChartLineFormat] = Field(default=None,alias="line",)

from .workbook_chart_line_format import WorkbookChartLineFormat

