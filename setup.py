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
VERSION = '0.2'
SUMMARY = 'Eases the transition from PIL to Pillow for projects.'

fp = open('README.rst', 'r')
DESCRIPTION = fp.read().strip()
fp.close()

PIL_WARNING = '''
***************************************************************************
The "PIL" library is deprecated in favor of "Pillow", and may not be
supported in a future release.

To switch to "Pillow", you must first uninstall "PIL".
***************************************************************************
'''


# If PIL is installed, use that. Otherwise prefer the newer Pillow library.
pil_req = pkg_resources.Requirement.parse('PIL')

try:
    pkg_resources.get_provider(pil_req)

    # We found PIL. So, guess we have to use that.
    sys.stderr.write('\n%s\n' % PIL_WARNING.strip())
    image_lib = 'PIL'
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
