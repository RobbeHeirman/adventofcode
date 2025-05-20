from abc import abstractmethod
from typing import TypeVar, Generic, Type, Any

import core.python.solution_meta as solution_meta

T = TypeVar("T")


class Solution(Generic[T], metaclass=solution_meta._SolutionMeta):
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
    def read_input(cls, lines: list[str]) -> T:
        pass

    @classmethod
    @abstractmethod
    def solution1(cls, inp: T) -> Any:
        pass

    @classmethod
    @abstractmethod
    def solution2(cls, inp: T) -> Any:
        pass
