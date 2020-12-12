import codecs
import os

import setuptools


long_description = ''
with codecs.open('./README.md', encoding='utf-8') as readme_md:
    long_description = readme_md.read()

with open('./requirements/base.txt') as reqs_txt:
    reqs = [line for line in reqs_txt]

with open('./requirements/test.txt') as test_reqs_txt:
    test_reqs = [line for line in test_reqs_txt]

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
    python_requires=">=3.8",
    install_requires=reqs,
    extras_require={
        "testing": test_reqs,
    },
    entry_points={
        "console_scripts": ["shifumi=shifumi.main:main"],
    },
)
