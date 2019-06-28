from typing import Callable


def mkint() -> int:
    return 42


def mkfloat() -> float:
    return 3.14


def process_float(fn: Callable[[], float]) -> None:
    x = fn()
    res = x ** .5
    print(f'{x} -> {res}')


def process_int(fn: Callable[[], int]) -> None:
    x = fn()
    res = x << 1
    print(f'{x} -> {res}')


# Callables are covariant in their return types. This means that we should be
# able to use a function that return an int where one that returns a float is
# expected (assuming that the arguments are the same).
process_float(mkint)

# The reverse is not true.
process_int(mkfloat)        # error!
