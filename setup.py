import setuptools
import re
import os

def find_version_author_mail():
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, "MLCrawl/__init__.py"), 'r') as fp:
        version_file = fp.read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    author_match = re.search(r"^__author__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    author, mail = re.split(r'<',author_match.group(1))
    return version_match.group(1), author.rstrip(), re.sub('>', '', mail)

version, author, mail = find_version_author_mail()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MLCrawl",
    version=version,
    author=author,
    author_email=mail,
    description="A focussed web crawler based on a One-class Support Vector Machine.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elpunkt/MLCrawl",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ),
)
