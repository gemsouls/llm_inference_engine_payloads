from typing import *

from pydantic import BaseModel, Field, Required


class AdditionalGenerationArguments(BaseModel):
    do_sample: bool = Field(default=False)
    min_tokens: int = Field(default=1)


class BaseTaskInputs(BaseModel):
    task_id: str = Field(default=Required)
    api_key: Optional[str] = Field(default=None)
    org_id: Optional[str] = Field(default=None)
    task_inputs: Any = Field(default=Required)
    additional_generation_arguments: AdditionalGenerationArguments = Field(default=AdditionalGenerationArguments())


class BaseTaskOutputs(BaseModel):
    task_id: str = Field(default=Required)
    task_outputs: Any = Field(default=Required)
    duration: float = Field(default=Required)
    statu_code: int = Field(default=Required)
    error_info: Optional[Any] = Field(default=None)
