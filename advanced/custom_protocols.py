# One can define custom protocols by subclassing typing.Protocol (or
# typing_extensions.Protocol for python 3.7 or earlier). Methods and attributes
# defined in the Protocol subclass are what define the protocol itself.
from typing import Protocol


class Event:
    pass


class AppDelegate(Protocol):
    def finished_launching(self, event: Event) -> None:
        ...             # <- note the missing implementation

    def should_terminate(self, event: Event) -> bool:
        """Called just before the app quits"""
        ...             # <- note the missing implementation


# Note the need to inherit from Protocol!
class NamedAppDelegate(AppDelegate, Protocol):
    name: str


class Application:
    delegate: AppDelegate


class Delegate:
    def __init__(self, name: str) -> None:
        self.name = name

    def finished_launching(self, event: Event) -> None:
        print(f'{self.name}: yippy!')

    def should_terminate(self, event: Event) -> bool:
        print(f'{self.name}: bye')
        return True


app = Application()
app.delegate = Delegate('foo')
