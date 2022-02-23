from setuptools import find_packages, setup

setup(
    name="validin",
    packages=find_packages(include=["validin"]),
    version="0.1.0",
    description="foo",
    author="Iarla Crewe",
    license="GNU GENERAL PUBLIC LICENSE",
    install_requires=[],
    setup_requires=["pytest-runner==5.3.1"],
    tests_require=["pytest==7.0.1"],
    test_suite="tests"
)