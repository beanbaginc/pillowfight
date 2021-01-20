#!/usr/bin/env python
import sys

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

import pkg_resources


NAME = 'pillowfight'
VERSION = '0.4'
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
    image_lib = 'Pillow>=3.4.2'

    if sys.hexversion < 0x02070000:
        # Pillow 4.0 requires Python 2.7+. For older versions of Python, we
        # can't go higher than 3.x.
        image_lib += ',<=3.9999'
    elif sys.hexversion < 0x03050000:
        # Pillow 7.0 requires Python 3.5+.
        image_lib += ',<=6.9999'

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
