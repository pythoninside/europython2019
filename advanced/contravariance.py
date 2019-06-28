# Callables are contravariant in their arguments. This means that one can, for
# instance, use a function that processes floats in a place where a function
# that processes integers is expected; but not the other way around.
from typing import Callable, TypeVar


T = TypeVar('T')


def proc_int(x: int) -> None:
    res = x << 1
    print(f'{x} -> {res}')


def proc_float(x: float) -> None:
    res = x ** .5
    print(f'{x} -> {res}')


def pipeline(x: T, fn: Callable[[T], None]) -> None:
    fn(x)


x: int = 42
pipeline(x, proc_float)     # OK
y: float = 3.14
pipeline(y, proc_int)       # Error
