from typing import *

from openai_api_payloads.chat_completion import ChatCompletionInputs, ChatCompletionOutputs
from pydantic import BaseModel, Field, Required

from .common import BaseTaskInputs, BaseTaskOutputs


class ChatCompletionTaskInputs(BaseTaskInputs):
    task_inputs: ChatCompletionInputs = Field(default=Required)


class ChatCompletionTaskOutputs(BaseTaskOutputs):
    task_outputs: ChatCompletionOutputs = Field(default=Required)
