# User-defined generics are considered invariant by default. We can, however,
# mark them as covariant or contravariant in their type if we so decide (and
# know what we are doing).
from typing import TypeVar, Generic


T_co = TypeVar('T_co', covariant=True)


class Foo(Generic[T_co]):
    def __init__(self, element: T_co) -> None:
        self._x = element

    def bar(self) -> None:
        print(f'self._x = {self._x}')


x: Foo[int] = Foo(42)
y: Foo[float] = Foo(3.14)

x = y           # Error: I cannot simply replace a Foo[int] by a Foo[float]
y = x           # But I can replace a Foo[float] by its subtype
# Similarly
tx = (1, 2, 3)
ty = (1., 2., 3.)
tx = ty         # Error: Tuple is covariant in its arguments
ty = tx         # OK
