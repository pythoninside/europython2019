# This is how you type annotate functions in Python 3.x code.
from typing import Callable


# Single argument
def square_root(x: float) -> float:
    return x ** .5


# Default values
def shift_left(x: int, places: int = 1) -> int:
    return x << places


# No return/return None
def greetings(name: str) -> None:
    print(f'Hello {name}')


# The type of a function/callable
fn: Callable[[int, int], int] = shift_left
