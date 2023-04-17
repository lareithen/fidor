from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='fidor.py',
    version='1.0',
    description='A generator for random words, sentences and paragraphs.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='larei',
    author_email='larei@nomail.com',
    url='https://github.com/lareithen/fidor',
    packages=find_packages(),
)
