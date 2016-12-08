"""The setup file for testing the trigrams module."""

from setuptools import setup

setup(
    name="trigrams",
    description="Create new works of text composed from trigrams of an input
    file.",
    author="Jordan Schatzman", "Rick Valenzuela",
    author_email="j.schatzman@outlook.com",
    license="MIT",
    py_modules=['trigrams'],
    install_requires=['io'],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']},
}
