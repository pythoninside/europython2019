# Unions are used for things that can be one type or another.
# Optionals are Unions which include None
from typing import List, Union, Optional


a_complex_list = [1, '2', 3, 4, '5']  # type: List[Union[int, str]]


# Sometimes we return something, other times nothing: Optionals!
# Optional[int] = Union[int, None]
def find_element_index(el, elements):
    # type: (int, List[int]) -> Optional[int]
    if el in elements:
        return elements.index(el)
    return None     # required by the type checker
