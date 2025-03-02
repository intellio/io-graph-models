from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field


class AccessPackageAnswer(BaseModel):
	displayValue: Optional[str] = Field(default=None,alias="displayValue",)
	answeredQuestion: Optional[AccessPackageQuestion] = Field(default=None,alias="answeredQuestion",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

	@model_validator(mode="wrap")
	def convert_discriminator_class(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
		try:
			# check with parent model to catch any errors
			parent_validated_model = handler(data)
			# check if the discriminator field is present
			if "@odata.type" not in data:
				return parent_validated_model
			# get the discriminator value
			mapping_key = data["@odata.type"]
			if mapping_key == "#microsoft.graph.accessPackageAnswerString":
				from .access_package_answer_string import AccessPackageAnswerString
				return AccessPackageAnswerString.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .access_package_question import AccessPackageQuestion

