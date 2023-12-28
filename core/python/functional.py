from typing import Callable, Iterable, TypeVar


def foreach(func: Callable[[any, ...], any], *args: [Iterable[any]]) -> None:
    for vals in zip(*args):
        func(*vals)

T = TypeVar("T")
def find_first(conditional: Callable[[T], bool], iterable: [Iterable[T]], default_value: T | None = None) -> T | None:
    for val in iterable:
        if conditional(val):
            return val
    return None