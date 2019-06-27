# None is a type witgh profound implications for the type checker
import traceback
from typing import Optional, TypeVar


# Use None as the return type of functions which do not return a value
def greet(name: str) -> None:
    print(f'Hello {name}')
    # No need for an explicit return here


# Do not assign the result of greet to a variable
foo = greet('Francesco')


AnyException = TypeVar('AnyException', bound=Exception)


# Beware when using Optionals (which can be None)
def print_traceback(ex: Optional[AnyException]) -> None:
    # traceback.print_tb(ex.__traceback__)  # type error: ex could be None!
    # The type checker understand these checks
    if ex:
        traceback.print_tb(ex.__traceback__)
