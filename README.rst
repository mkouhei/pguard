========
 pguard
========

Guard like Haskell for Python.

Status
======

.. image:: https://secure.travis-ci.org/mkouhei/pguard.png?branch=master
   :target: http://travis-ci.org/mkouhei/pguard
.. image:: https://coveralls.io/repos/mkouhei/pguard/badge.png?branch=master
   :target: https://coveralls.io/r/mkouhei/pguard?branch=master
.. image:: https://img.shields.io/pypi/v/pguard.svg
   :target: https://pypi.python.org/pypi/pguard
.. image:: https://readthedocs.org/projects/pguard/badge/?version=latest
   :target: https://readthedocs.org/projects/pguard/?badge=latest
   :alt: Documentation Status

Requirements
============

* Python 2.7 or Python 3.3 over or PyPy 2.4.0 over

Features
========

* guard with lambda

Setup
=====

::

  $ pip install --user pguard
  or
  (venv)$ pip install pguard

Usage
=====

::

   >>> from pguard import guard
   >>> from pguard import guard_cl as g
   >>> (lambda n: guard(
   ... g(-1, n < 0),
   ... g(0, n == 0),
   ... g(1)  ## otherwise
   ... ))(0)
   0

