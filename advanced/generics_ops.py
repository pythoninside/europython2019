# Can we just mix and match generics of a type and a subtype? Noty a trivial
# question, as this example illustrates.
from typing import List, Tuple


def shift_left_list(xs: List[int]) -> List[int]:
    return [x << 1 for x in xs]


def shift_left_tuple(xs: Tuple[int, ...]) -> Tuple[int, ...]:
    return tuple(x << 1 for x in xs)


shift_left_list([1., 2., 3.])
shift_left_tuple((1., 2., 3.))
