import os
from setuptools import setup, find_packages

version = "0.1.0"
requirements = [
    "pydantic",
    f"openai_api_payloads @ https://github.com/gemsouls/openai_api_payloads/releases/download/v1.0.0/openai_api_payloads-1.0.0-py3-none-any.whl"
]
include_dirs = ["deps"]


setup(
    name="llm_inference_engine_payloads",
    package_dir={"": "src"},
    packages=find_packages("src"),
    version=version,
    install_requires=requirements,
    include_dirs=include_dirs
)
