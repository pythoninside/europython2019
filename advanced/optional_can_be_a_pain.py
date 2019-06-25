from typing import Optional, List


def find_element_index(el: int, elements: List[int]) -> Optional[int]:
    if el in elements:
        return elements.index(el)
    return None     # required by the type checker


x = 3
xs = [1, 2, 3, 4, 5, 6]
i = find_element_index(x, xs)
print(f'{x} is element number {i + 1} of {xs!r}')  # mypy error
