# -*- coding: utf-8 -*-
"""Guard like Haskell for Python."""
import sys
import inspect

__version__ = '0.2.0'


def _has_args(func):
    if sys.version_info < (3, 3):
        return len(inspect.getargspec(func).args) > 0
    else:
        return len(inspect.signature(func).parameters) > 0


def _evaluate(statement, params=None):
    if inspect.isfunction(statement) or inspect.ismethod(statement):
        if _has_args(statement):
            if params is not None:
                evaluation = statement(*params)
            else:
                raise Exception('Invalid parameters.')
        else:
            evaluation = statement()
    else:
        evaluation = statement
    return evaluation


def guard_cl(statement, condition=None, params=None):
    """guard clause.

    :return: any value or False.

    :param statement: expression statement.
    :param condition: condition statement.
    :param tuple params: expression statement parameters.

    >>> (lambda n: (
    ... guard_cl(-1, n < 0),
    ... guard_cl(0, n == 0),
    ... guard_cl(1)))(0)
    (False, 0, 1)

    >>> def foo(x):
    ...     return x + 1

    >>> (lambda n: (
    ... guard_cl(foo, n == 0, (n,)),
    ... guard_cl(foo, n == 1, (n,)),
    ... guard_cl('out of range')
    ... ))(0)
    (1, False, 'out of range')

    >>> [(lambda n: guard(
    ... guard_cl(foo, n == 0, (n,)),
    ... guard_cl(foo, n == 1, (n,)),
    ... guard_cl('out of range')
    ... ))(i) for i in range(0, 4)]
    [1, 2, 'out of range', 'out of range']

    >>> (lambda n: (guard_cl(foo, n == 2)))(2)
    Traceback (most recent call last):
    ...
    Exception: Invalid parameters.

    >>> def bar():
    ...     return 'noop'

    >>> (lambda n: guard_cl(bar, n == 2))(2)
    'noop'

    >>> def baz(x, y):
    ...     return x + y

    >>> (lambda i, j: (
    ... guard_cl(baz, True, (i, j))
    ... ))(10, 5)
    15
    """
    evaluation = _evaluate(condition, params)
    if evaluation is not False or evaluation is None:
        return _evaluate(statement, params)
    else:
        return False


def guard(*guard_clauses):
    """guard function.

    :param tuple *guard_clauses: guard clauses.

    >>> g = guard_cl
    >>> (lambda n: guard(
    ... g(-1, n < 0),
    ... g(0, n == 0),
    ... g(1)  ## otherwise
    ... ))(0)
    0

    >>> s = lambda n: guard(
    ... g(-1, n < 0),
    ... g(0, n == 0),
    ... g(1)  ## otherwise
    ... )
    >>> [s(i) for i in [-10, 3, 0, 1, -12.0, 2]]
    [-1, 1, 0, 1, -1, 1]
    >>> s2 = lambda n: guard(
    ... g(-1, n < 0),
    ... g(0, n == 0),
    ... )
    >>> [s2(i) for i in [-10, 3, 0, 1, -12.0, 2]]
    [-1, False, 0, False, -1, False]

    >>> def fibo(n):
    ...    if n < 0 : return -1
    ...    if n == 0 or n == 1: return 1
    ...    return fibo(n - 1) + fibo(n - 2)
    >>> f = lambda n: guard(
    ... g(Exception('out of range'), n < 0),
    ... g(1, n < 2),
    ... g(fibo(n - 1) + fibo(n - 2))
    ... )
    >>> [f(i) for i in range(-1, 10)]
    [Exception('out of range',), 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    >>> b = lambda w, h: guard(
    ... g('Very severely underweight', w / h ** 2 < 15.0),
    ... g('Severely underweight', w / h ** 2 < 16.0),
    ... g('Underweight', w / h ** 2 < 18.5),
    ... g('Normal (healthy weight)', w / h ** 2 < 25.0),
    ... g('Overweight', w / h ** 2 < 30.0),
    ... g('Obese Class I (Moderately obese)', w / h ** 2 < 35.0),
    ... g('Obese Class II (Severely obese)', w / h ** 2 < 40.0),
    ... g('Obese Class III (Very severely obese)')
    ... )
    >>> b(67.3, 1.68)
    'Normal (healthy weight)'
    """
    for _guard in guard_clauses:
        if _guard is not None and _guard is not False:
            return _guard
    return False
