Pillow Fight
============

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


Who's using it
--------------

We're using it for our code review product,
[Review Board](http://www.reviewboard.org/).

If you're using it, [let us know](mailto:christian@beanbaginc.com).
