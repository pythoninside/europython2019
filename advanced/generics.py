# We can use type variables to create generic types ourselves. We have already
# seen the use of type variables in generic types in the typing module like
# e.g., List[T] or Dict[T, S]
from typing import Generic, List, TypeVar

T = TypeVar('T')


class Vector(Generic[T]):
    def __init__(self, elements: List[T]) -> None:
        self.elements = elements

    def pop(self) -> T:
        return self.elements.pop()


# We can also define generic functions
def head(v: Vector[T]) -> T:
    # return v[0]   # error: Vector does not define __getitem__
    return v.elements[0]
