from abc import abstractmethod, ABCMeta
from typing import TypeVar, Generic, Type, Any

T = TypeVar("T")


class _SolutionMeta(ABCMeta):

    def __new__(mcs: Type["Solution"], name, bases, *args, **kwargs):
        c = super().__new__(mcs, name, bases, *args, **kwargs)
        if bases and isinstance(c, Solution):
            mcs._print_solution(c)
        return c

    def _print_solution(cls: Type["Solution"]):
        solvers = {
            "1": cls.solution1,
            "2": cls.solution2
        }
        lines = cls.read_file()
        inp = cls.read_input(lines)
        for key, val in solvers.items():
            print(f"Solution for {cls.__name__}, part {key} is {val(inp)}")


class Solution(Generic[T], metaclass=_SolutionMeta):
    """
    Does some IO boilerplate. basic parsing of input file. Looks for __filename__=input.txt in workdir.
    If you want another __filename__ just overwrite this variable in subclass definition.
    parses file to string list representing file lines.
    Prints results of solution 1 and solution 2.

    Use as follows:
        - subclass Solution
        - implement read_input and transform how you want to pass to solution functions.
        - implement solution 1
        - implement solution 2
        - Run script of  class or import somewhere.
    Metaclass will (dirty) call solutions during instantiation of subclass.
    """

    __filename__ = "input.txt"

    @classmethod
    def read_file(cls: Type["Solution"]) -> [str]:
        with open(cls.__filename__) as f:
            return f.read().splitlines()

    @classmethod
    @abstractmethod
    def read_input(cls, lines: [str]) -> T:
        ...

    @classmethod
    @abstractmethod
    def solution1(cls, inp: T) -> Any:
        ...

    @classmethod
    @abstractmethod
    def solution2(cls, inp: T) -> Any:
        ...

