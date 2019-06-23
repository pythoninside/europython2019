# Some tricks and random convenience stuff
from typing import Iterator


# Positional-only args in callables with __
def irange(__n: int) -> Iterator[int]:
    i = 0
    while i < __n:
        yield i
        i += 1


print(list(irange(n=10)))     # mypy error


# Convenience shorthand for *args and **kwargs
def foo(*args: int, **kwargs: str) -> None:
    print('Hi there')


foo(1, 2, 3, a='bar', b='baz')
