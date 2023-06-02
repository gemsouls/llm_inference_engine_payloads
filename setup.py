import os
from setuptools import setup, find_packages


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DEP_DIR = os.path.join(PROJECT_ROOT, "deps")

version = "0.1.0"
requirements = [
    "pydantic",
    f"openai_api_payloads @ file://localhost/{os.path.join(DEP_DIR, 'openai_api_payloads-1.0.0-py3-none-any.whl')}"
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
