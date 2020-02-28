# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r") as f:
    readme = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="era5analysis",
    version="0.0.1",
    author="Alexander Kuhn-Regnier",
    author_email="ahf.kuhnregnier@gmail.com",
    description="Download and analyse ERA5 data from the Climate Data Store.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/akuhnregnier/era5analysis",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
)
