Release Notes
=============

.. |PIOCONF| replace:: `"platformio.ini" <https://docs.platformio.org/en/latest/projectconf.html>`__ configuration file
.. |LDF| replace:: `LDF <https://docs.platformio.org/en/latest/librarymanager/ldf.html>`__
.. |INTERPOLATION| replace:: `Interpolation of Values <https://docs.platformio.org/en/latest/projectconf/interpolation.html>`__
.. |UNITTESTING| replace:: `Unit Testing <https://docs.platformio.org/en/latest/advanced/unit-testing/index.html>`__

.. _release_notes_6:

QIO Core 6
-----------------

**A professional collaborative platform for declarative, safety-critical, and test-driven embedded development.**

6.1.6 (2023-02-01)
~~~~~~~~~~~~~~~~~~

* Added support for Python 3.11
* Made assets (templates, ``99-platformio-udev.rules``) part of Python's module (`issue #4458 <https://github.com/platformio/platformio-core/issues/4458>`_)
* Updated `Clang-Tidy <https://docs.platformio.org/en/latest/plus/check-tools/clang-tidy.html>`__ check tool to v15.0.5 with new diagnostics and bugfixes
* Removed dependency on the "zeroconf" package and install it only when a user lists mDNS devices (issue with zeroconf's LGPL license)
* Show the real error message instead of "Can not remove temporary directory" when "platform.ini" is broken (`issue #4480 <https://github.com/platformio/platformio-core/issues/4480>`_)

