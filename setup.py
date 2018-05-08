from setuptools import find_packages, setup

VERSION = __import__("import_export").__version__

setup(
    name='test-semantic-release',
    version=VERSION,
    url='https://github.com/bmihelac/test-semantic-release/',
    author='Bojan Mihelac',
    author_email='bmihelac@mihelac.org',
    description='Description of my package',
    packages=find_packages(),
    install_requires=[],
)
