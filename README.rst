Pillow Fight
============

Pillow is a replacement for PIL that works as a drop-in replacement. Unlike
PIL, it's actively maintained and easy to install. It's pretty great. There's
only one problem, which is that users must first uninstall PIL before
installing Pillow, as they share a namespace.

This makes it very hard for Python modules or products that need to run on a
variety of configurations to easily depend on either PIL or Pillow without
inevitably breaking something (perhaps in subtle ways). That makes it hard to
safely  transition.

This package aims to "solve" that by providing a single dependency that can
intelligently depend on either PIL or Pillow, based on what's already on the
system. Packages that still need to work if PIL is installed, but aim to
transition to Pillow, can simply depend on the ``pillowfight`` package.


How it works
------------

This package is provided as a source distribution with a simple setup script.
When ``pillowfight`` is installed for the first time, its setup script will
run and start inspecting the system.

The setup script will look to see if PIL is already installed. If so, it will
print a warning saying that PIL is deprecated and to install Pillow. It will
then turn around and depend on PIL.

If PIL is not installed, it will instead depend on Pillow.


Using pillowfight
-----------------

Simply replace your PIL dependency with ``pillowfight`` in ``setup``'s
``install_requires`` list:

.. code-block:: python

    setup(name='MyPackage',
          version='1.0',
          install_requires=[
              'pillowfight'
          ]
    )


Why we wrote this
-----------------

We use Django and Pillow for a product that sysadmins can install in their
networks. There are a lot of configurations out there, and a lot of older
systems already using PIL.

We've been trying to figure out the right strategy for getting new and
existing users onto Pillow without breaking any installs. We don't have much
control over their systems, so we knew we had to be clever.

A lot of projects out there seem to have modified their ``setup.py`` files to
check what's on the system, but in practice, that doesn't work too well. When
building Python eggs, the ``requires.txt`` files would be populated with
either ``PIL`` or ``Pillow``, and that just wasn't going to work.

So we wrote this as a way to have a stable dependency that could do the right
thing. We hope others will find it useful.


Who's using it
--------------

We're using it for our code review product,
`Review Board <http://www.reviewboard.org/>`_.

If you're using it, `let us know <mailto:christian@beanbaginc.com>`_.
