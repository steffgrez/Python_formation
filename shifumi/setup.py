import os
import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

deps = [
    "tinydb==4.2.0",
    "PyYAML==5.3.1",
]

test_deps = [
    "black",
    "pytest",
    "coverage",
    "pytest-cov",
    "pylint",
    "xenon",
]
extras = {
    "testing": test_deps,
}

setuptools.setup(
    name="shifumi",
    version="1.1.0",
    author="Stéphane Lahache",
    author_email="slahache@mail.com",
    description="my shifumi game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/steffgrez/Python_formation",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=deps,
    tests_require=test_deps,
    extras_require=extras,
    entry_points={
        "console_scripts": ["shifumi=shifumi.main:main"],
    },
)
