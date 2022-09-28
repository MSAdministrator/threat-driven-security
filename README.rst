Threat Driven Security
======================

|PyPI| |Status| |Python Version| |License|

|Read the Docs| |Tests| |Codecov|

|pre-commit| |Black|

.. |PyPI| image:: https://img.shields.io/pypi/v/threat-driven-security.svg
   :target: https://pypi.org/project/threat-driven-security/
   :alt: PyPI
.. |Status| image:: https://img.shields.io/pypi/status/threat-driven-security.svg
   :target: https://pypi.org/project/threat-driven-security/
   :alt: Status
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/threat-driven-security
   :target: https://pypi.org/project/threat-driven-security
   :alt: Python Version
.. |License| image:: https://img.shields.io/pypi/l/threat-driven-security
   :target: https://opensource.org/licenses/MIT
   :alt: License
.. |Read the Docs| image:: https://img.shields.io/readthedocs/threat-driven-security/latest.svg?label=Read%20the%20Docs
   :target: https://threat-driven-security.readthedocs.io/
   :alt: Read the documentation at https://threat-driven-security.readthedocs.io/
.. |Tests| image:: https://github.com/MSAdministrator/threat-driven-security/workflows/Tests/badge.svg
   :target: https://github.com/MSAdministrator/threat-driven-security/actions?workflow=Tests
   :alt: Tests
.. |Codecov| image:: https://codecov.io/gh/MSAdministrator/threat-driven-security/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/MSAdministrator/threat-driven-security
   :alt: Codecov
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black


Goals
--------

Determine an organizations security visibility from simple description of log sources in an environment.


1. Define a list of common threat scenarios / potential tabletop exercises
2. Do I have visibility to detect this scenario
   1. Could I have detected it earlier?


## Questions for consumer


1. Product Exchange, Mail Flow Logs, User Reported Phishing Messages, and _some_ DLP Logs
   1. Confidence - 4




This project aims to assist organizations with a common framework to identify their defensive visibility.

By utilizing a community sourced set of common threat definitions facing organizations we can identify
different aspects (view points) of a threat in a vendor agnostic way. This allows organizations to understand
gaps in their visibility so they can defend against these threats appropriately.

1. Reviewing products for security auditing
   1. UC: Enables organizations to validate that the products they are looking at have the minimum requirements based on definitions
   2. UC: Architecture Auditing?



Features
--------

* TODO


Requirements
------------

* TODO


Installation
------------

You can install *Threat Driven Security* via pip_ from PyPI_:

.. code:: console

   $ pip install threat-driven-security


Usage
-----

Please see the `Command-line Reference <Usage_>`_ for details.


Contributing
------------

Contributions are very welcome.
To learn more, see the `Contributor Guide`_.


License
-------

Distributed under the terms of the `MIT license`_,
*Threat Driven Security* is free and open source software.


Issues
------

If you encounter any problems,
please `file an issue`_ along with a detailed description.


Credits
-------

This project was generated from `@cjolowicz`_'s `Hypermodern Python Cookiecutter`_ template.

.. _@cjolowicz: https://github.com/cjolowicz
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _MIT license: https://opensource.org/licenses/MIT
.. _PyPI: https://pypi.org/
.. _Hypermodern Python Cookiecutter: https://github.com/cjolowicz/cookiecutter-hypermodern-python
.. _file an issue: https://github.com/MSAdministrator/threat-driven-security/issues
.. _pip: https://pip.pypa.io/
.. github-only
.. _Contributor Guide: CONTRIBUTING.rst
.. _Usage: https://threat-driven-security.readthedocs.io/en/latest/usage.html
