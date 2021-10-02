"""The setup script."""

from setuptools import find_packages, setup

from lib_template import __version__

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()
with open("requirements_tests.txt") as f:
    test_requirements = f.read().splitlines()

setup(
    author="Aritra Biswas",
    author_email="pandalearnstocode@gmail.com",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    description="Pythoon Library template for Data Science project.",
    entry_points={
        "console_scripts": [
            "lib_template=lib_template.cli:main",
        ],
    },
    install_requires=requirements,
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="lib_template",
    name="lib_template",
    packages=find_packages(include=["lib_template", "lib_template.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/ab-inbev-martech-analytics/lib_template",
    version=__version__,
    zip_safe=False,
)