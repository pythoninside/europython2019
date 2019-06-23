# Python 3.6+ only style
from typing import Tuple


def fast_fib(n: int) -> int:
    assert n >= 0, 'Expecting a non-negative integer'

    seq: Tuple[int, int, int]
    seq = (0, 1, 1)
    if n < 3:
        return seq[n]

    nminustwo: int = 1
    nminusone: int = 1
    for i in range(3, n + 1, 1):
        nminusone, nminustwo = nminustwo + nminusone, nminusone
    return nminusone


def slow_fib(n: int) -> int:
    if n < 0:
        raise ValueError('Expecting a non-negative integer')

    seq: Tuple[int, int, int] = (0, 1, 1)
    if n < 3:
        return seq[n]

    return slow_fib(n - 2) + slow_fib(n - 1)


print(fast_fib(-1))
