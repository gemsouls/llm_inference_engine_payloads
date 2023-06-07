from setuptools import setup, find_packages

version = "0.2.0"
requirements = [
    "pydantic",
    "openai_api_payloads @ https://github.com/gemsouls/openai_api_payloads/releases/download/v1.0.1/openai_api_payloads-1.0.1-py3-none-any.whl"
]


setup(
    name="llm_inference_engine_payloads",
    package_dir={"": "src"},
    packages=find_packages("src"),
    version=version,
    install_requires=requirements
)
