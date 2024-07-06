from setuptools import setup
from setuptools import find_packages

with open('requirements.txt') as f: 
    content = f.readlines()
requirements = [x.strip() for x in content]

setup(name='tata',
      description="package description",
      packages=["tata"],
      install_requires=requirements)
