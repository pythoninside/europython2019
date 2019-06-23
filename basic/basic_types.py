# Built-in types are used as is in type annotations. However collections,
# mappings, sets etc. need to be imported from the typing module.
from typing import Tuple, List, Set, Dict


# Built-in types
an_integer: int = 1
a_float: float = 1.2
a_string: str = 'Hello there!'
some_bytes: bytes = b'Hello there!'
a_boolean: bool = False

# Simple collections
a_list: List[int] = [1, 2, 3]
a_set: Set[int] = {1, 2, 3}

# Tuples can be heterogeneous
a_tuple: Tuple[int, str, bool] = (1, 'foo', True)

# Dictionaries need types for keys and values
a_dict: Dict[str, float] = {'one': 1.0, 'two': 2.0}
