from setuptools import setup, find_packages

setup(
    name="llm_logger",
    version="0.1.0",
    packages=find_packages(exclude=["tests"]),
    author="enes",
    author_email="enesbasbugai@gmail.com",
    description="This open-source logger library is designed for use with LLM applications. Its purpose is to track the behavior of LLMs (Large Language Models) by logging their inputs and outputs.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/enesbasbug/llm_logger",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)