from typing import *

from pydantic import BaseModel, Field, Required


class AdditionalGenerationArguments(BaseModel):
    do_sample: bool = Field(default=False)
    min_tokens: int = Field(default=1)
    max_tokens: Optional[int] = Field(default=None)
    num_beams: Optional[int] = Field(default=None)
    num_return_sequences: Optional[int] = Field(default=None)


class ErrorBody(BaseModel):
    error_type: str = Field(default=Required)
    error_message: str = Field(default=Required)


class BaseTaskInputs(BaseModel):
    task_id: str = Field(default=Required)
    api_key: Optional[str] = Field(default=None)
    org_id: Optional[str] = Field(default=None)
    task_inputs: Any = Field(default=Required)
    additional_generation_arguments: AdditionalGenerationArguments = Field(default=AdditionalGenerationArguments())
    user_id: Optional[str] = Field(default=None)
    adapter_id: Optional[str] = Field(default=None)


class BaseTaskOutputs(BaseModel):
    task_id: str = Field(default=Required)
    task_outputs: Any = Field(default=Required)
    duration: float = Field(default=Required)
    status: int = Field(default=Required)
    errors: Optional[List[ErrorBody]] = Field(default=None)
