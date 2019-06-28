# When using generics one has to be a bit careful. It is often times not clear
# if one can safely use a generic of given types where the same generic but of
# sub-types or super-types is expected. Which generics we can safely use where
# is determined by their variance wrt their types.
from typing import TypeVar, Callable, List


T = TypeVar('T')


def pipeline(data: List[T], data_processor: Callable[[T], T]) -> None:
    """A simple data pipeline. """
    for el in data:
        res = data_processor(el)
        print(f'{el} -> {res}')


def int_proc(n: int) -> int:
    """Some operation not available to floats."""
    return n << 1


def float_proc(x: float) -> float:
    return x ** .5


# Can we use List[int] where List[float] is expected?
ints: List[int] = [1, 2, 3, 4, 5]
floats: List[float] = [1., 2., 3., 4., 5.]
pipeline(floats, int_proc)          # Error
pipeline(ints, float_proc)          # Error
