# We can tell the checker to believe us or to stop type checking
from typing import Any, List, Dict, cast


a: List     # equivalent to List[Any]
b: Dict     # equivalent to Dict[Any, Any]

a = [1, 'foo']
# a = 123   # this would fail
b = {'a': 1, 'b': 'foo'}
c = cast(str, a)    # mypy belives us
c << 2      # mypy error as it assumes c to be a string
c += 3      # type: ignore


def foo(x: Any) -> str:
    print(x + 1)    # not type-checked
    return x        # not type-checked, but return necessary
