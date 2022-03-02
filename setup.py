from setuptools import find_packages, setup

setup(
    name="validin",
    packages=find_packages(include=["validin"]),
    version="0.6.0",
    description="Console input validator for python, allows for any condition to be checked in a clean and consice syntax",
    author="Iarla Crewe",
    license="GNU General Public License v3.0",
    install_requires=[],
    setup_requires=["pytest-runner==5.3.1"],
    tests_require=["pytest==7.0.1"],
    test_suite="tests"
)