from dataclasses import dataclass
from typing import Any

from core.python.solution import Solution, T



@dataclass
class ProblemSpace:
    updates:
    order: list[int]




class Day5(Solution):
    @classmethod
    def read_input(cls, lines: [str]) -> T:
        first, second = lines[:lines.index("")], lines[lines.index("") + 1:]
        f = map(lambda x: x.split("|"), first)
        f = [UpdateOrder(int(x[0]), int(x[1])) for x in f]

        s = ",".join(second)
        s = s.split(",")
        s = list(map(int, s))
        return ProblemSpace(f, s)

    @classmethod
    def solution1(cls, inp: T) -> Any:
        pass

    @classmethod
    def solution2(cls, inp: T) -> Any:
        pass
