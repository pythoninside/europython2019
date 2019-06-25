# Type variables are just like regular variable, only for types (i.e. things
# like int, float, User, List, etc.).
from typing import MutableSequence, TypeVar


class Animal:
    pass


class Dog(Animal):
    pass


class Cat(Animal):
    pass


# Define an unbound type variable
T = TypeVar('T')        # <- can be any type

# Now a bound type variable (it is actually already in the typing module, btw)
AnyStr = TypeVar('AnyStr', str, bytes)  # <- can be either str or bytes

# And finally a type variable with an upper bound
AnyAnimal = TypeVar('AnyAnimal', bound=Animal)


def append(x: T, xs: MutableSequence[T]) -> None:
    return xs.append(x)


def concatenate(s1: AnyStr, s2: AnyStr) -> AnyStr:
    return s1 + s2


def greet(animal: AnyAnimal) -> None:
    print(f'Hello {animal.__class__.__name__.lower()}')
