from pathlib import Path

from setuptools import setup

PROJECT_NAME = "qwilib"
PROJECT_ROOT = Path(__file__).parent
SOURCE_ROOT = PROJECT_ROOT / PROJECT_NAME
RESOURCES = f"{str(SOURCE_ROOT / 'resources' / 'icons')}/*"

with open(str(PROJECT_ROOT / "requirements.txt"), "r") as file:
    REQUIREMENTS = file.readlines()

setup(
    name=PROJECT_NAME,
    version="0.1.0",
    author="Izzat Z.",
    author_email="<izzat.zainir11@gmail.com>",
    description="An opinionated Qt Widgets library.",
    long_description_content_type="text/markdown",
    long_description="A Python library that attempts to pre-define some Qt Widgets (based on PySide6) for ease of "
                     "development.",
    packages=[PROJECT_NAME],
    package_data={PROJECT_NAME: [RESOURCES]},
    include_package_data=True,
    install_requires=REQUIREMENTS,
    keywords=[
        "python",
        "library",
        "qt",
        "widgets",
        "development"
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
    ]
)
