from setuptools import find_packages, setup

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: students & scientists",
    "Operating System :: OS Independent",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
]

setup(
    name="menage_jupyter.py",
    version="0.1.4",
    description="Package help menage jupyter files. It let convert py to jupyter file and vice versa, and clean jupyter output. Useful to exclude git conflicts",
    long_description=open("README.md").read() + "\n",
    url="",
    author="chwilko",
    author_email="bartekchwilkowski@gmail.com",
    license="MIT",
    classifiers=classifiers,
    keywords="jupyter",
    packages=find_packages(),
    install_requires=[],
)
