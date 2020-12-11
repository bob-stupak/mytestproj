#
#
from setuptools import setup
import os
import sys

if sys.version_info[0] < 3:
  with open('README.rst') as f:
    long_description = f.read()
else:
  with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

version={}
with open(os.path.join('mytestproj','_version.py')) as f:
  exec(f.read(),version)

setup(name='mytestproj',
      version=version['__version__'],
      description='Test function for learning setup',
      long_description=long_description,
      url='http://github.com/bob-stupak/testpackage',
      author='Bob Stupak',
      author_email='bob.stupak@noirlab.edu',
      license='MIT',
      packages=['mytestproj'],
      install_requires=['numpy==1.11.2',
                        'matplotlib==1.5.2',
                       ],
      zip_safe=False)

