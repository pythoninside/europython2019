from typing import Callable


# The type of a function/callable
# Types in lambdas are usually inferred and not annotated
fn: Callable[[int, int], int] = lambda x, y: x + y


# Callable object with any number and type of argument
decorator: Callable[..., int]
