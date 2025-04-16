from setuptools import setup, find_packages

setup(
    name="pr_generator",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "annotated-types==0.7.0",
        "anyio==4.9.0",
        "certifi==2025.1.31",
        "charset-normalizer==3.4.1",
        "GitPython==3.1.42",
        "langchain-core==0.3.51",
        "langchain-openai==0.3.12",
        "openai==1.72.0",
        "python-dotenv==1.1.0",
        "PyJWT==2.10.1"
    ],
    entry_points={
        'console_scripts': [
            'pr-generator=pr_generator.pr_generator:main',
        ],
    },
)