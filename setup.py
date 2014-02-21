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
DESCRIPTION = '''
PIL </3 Pillow
--------------

Pillow is a new replacement for PIL that works as a drop-in replacement. It's
great, but unfortunately, users must first uninstall PIL before installing
Pillow, or Bad Things Happen. This makes it very hard for public projects to
easily depend on one or the other without inevitably breaking something.

This package aims to "solve" that by providing a single dependency that can
intelligently depend on the appropriate package. Packages that need to maintain
compatibility with both can simply depend on the ``pillowfight`` package.

How it works
------------

This package is provided as a source distribution, meaning that it will be
pulled down and executed by any project depending on it.

The setup script will then look to see if PIL is already installed. If so,
it will spit out a warning about PIL being deprecated, and then depend on PIL.
The job is then done, and the project can be sure they have something that
works, even if it's not ideal.

If PIL is not installed, it will instead depend on Pillow.
'''.strip()


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
