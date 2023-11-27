from abc import abstractmethod, ABCMeta
from typing import TypeVar, Generic

T = TypeVar("T")


class SolutionMeta(Generic[T], ABCMeta):
    __day__ = 0

    def __new__(cls, name, bases, dct):
        c = super().__new__(cls, name, bases, dct)
        if bases:
            cls._print_solution(c)
        return c

    def _print_solution(cls: "SolutionMeta"):
        solvers = {
            "1": cls.solution1,
            "2": cls.solution2
        }
        inp = cls.read_input()
        for key, val in solvers.items():
            print(f"Solution for day {cls.__day__}, part {key} is {val(inp)}")

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
    def read_input(cls) -> T:
        ...


class Solution(metaclass=SolutionMeta):
    pass
