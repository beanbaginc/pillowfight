#!/usr/bin/env python
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

import pkg_resources


NAME = 'pillowfight'
VERSION = '0.1'
SUMMARY = 'Eases the transition from PIL to Pillow for projects.'

fp = open('README.rst', 'r')
DESCRIPTION = fp.read().strip()
fp.close()


# If PIL is installed, use that. Otherwise prefer the newer Pillow library.
pil_req = pkg_resources.Requirement.parse('PIL')

try:
    pkg_resources.get_provider(pil_req)

    # We found PIL. So, guess we have to use that.
    image_lib = 'PIL'

    sys.stderr.write('The "PIL" library is deprecated and support will be '
                     'removed in a future release.\n'
                     'To switch to "Pillow", you must first uninstall '
                     '"PIL".\n\n')
except pkg_resources.DistributionNotFound:
    image_lib = 'Pillow'


setup(name=NAME,
      version=VERSION,
      license='MIT',
      description=SUMMARY,
      long_description=DESCRIPTION,
      install_requires=[image_lib],
      zip_safe=True,
      url='https://github.com/beanbaginc/pillowfight',
      maintainer='Beanbag, Inc.',
      maintainer_email='support@beanbaginc.com')
