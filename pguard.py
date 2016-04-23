# -*- coding: utf-8 -*-
"""Guard like Haskell for Python."""


__version__ = '0.1.0'


def guard_cl(statement, condition=None):
    """guard clause.

    :return: any value or False.

    :param statement: expression statement.
    :param condition: condition statement.

    >>> (lambda n: (
    ... guard_cl(-1, n < 0),
    ... guard_cl(0, n == 0),
    ... guard_cl(1)))(0)
    (False, 0, 1)
    """
    if condition or condition is None:
        return statement
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
    """
    for _guard in guard_clauses:
        if _guard is not None and _guard is not False:
            return _guard
    return False
