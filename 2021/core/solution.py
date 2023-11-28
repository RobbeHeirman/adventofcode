from abc import abstractmethod, ABCMeta
from typing import TypeVar, Generic

T = TypeVar("T")


class SolutionMeta(Generic[T], ABCMeta):
    """
    Used for AdventOfCode
    Metaclass that auto prints solutions 1 and 2 on initializing a class of type SolutionMeta.
    Use as follows:
        - subclass Solution
        - implement solution 1
        - implement solution 2
        - Run script of  class or import somewhere.

    """

    __filename__ = 'input.txt'

    def __new__(mcs, name, bases, *args, **kwargs):
        c = super().__new__(mcs, name, bases, *args, **kwargs)
        if bases:
            mcs._print_solution(c)
        return c

    def _print_solution(cls: "SolutionMeta"):
        solvers = {
            "1": cls.solution1,
            "2": cls.solution2
        }
        lines = cls.read_file()
        inp = cls.read_input(lines)
        for key, val in solvers.items():
            print(f"Solution for {cls.__name__}, part {key} is {val(inp)}")

    def read_file(cls) -> [str]:
        with open(cls.__filename__) as f:
            return f.read().splitlines()

    @classmethod
    @abstractmethod
    def solution1(cls, inp: T):
        ...

    @classmethod
    @abstractmethod
    def solution2(cls, inp: T):
        ...

    @classmethod
    @abstractmethod
    def read_input(cls, lines: [str]) -> T:
        ...


class Solution(metaclass=SolutionMeta):
    @classmethod
    @abstractmethod
    def solution1(cls, inp: T):
        ...

    @classmethod
    @abstractmethod
    def solution2(cls, inp: T):
        ...

    @classmethod
    @abstractmethod
    def read_input(cls, lines: [str]) -> T:
        ...
