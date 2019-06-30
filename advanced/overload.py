from typing import Optional, overload


# As we have seen, Optional is handy but the type checker is not able to
# resolve branches which can only be known at runtime. We can avoid some
# runtime checks that the use of Optionals would force by overloading our
# function. This is of course not always possible.

# Note: the overload-decorated functions are not used at runtime.


class User:
    _id: int

    def __init__(self, user_id: int):
        self._id = user_id

    @classmethod
    def mkuser(cls, user_id: int) -> 'User':
        return User(user_id)


# Example: the create_user function could be defined with Optionals only but a
# better solution could be this:
@overload
def create_user(user_id: None) -> None:
    ...         # <- note the ellipsis


@overload
def create_user(user_id: int) -> User:
    ...         # <- note the ellipsis


# Implementation
def create_user(user_id: Optional[int]) -> Optional[User]:
    if user_id is None:
        return None
    return User.mkuser(user_id)


user = create_user(123)
_ = create_user(None)


# The case below, however is not easily addressed by using overloaded funcs.
# def find_element_index(el: int, elements: List[int]) -> Optional[int]:
#     if el in elements:
#         return elements.index(el)
#     return None     # required by the type checker
