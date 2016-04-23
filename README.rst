========
 pguard
========

Guard like Haskell for Python.

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
