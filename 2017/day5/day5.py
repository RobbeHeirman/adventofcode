from itertools import count
from typing import Any

import core.python.solution as solution
from core.python.solution import T

class Day5(solution.Solution):
    @classmethod
    def read_input(cls, lines: [str]) -> list[int]:
        return [int(l) for l in lines]

    @classmethod
    def solution1(cls, inp: list[int]) -> int:
        p_c = 0
        for steps in count(1):
            p_c += inp[p_c]
            print(p_c)
            if p_c >= len(inp):
                return steps
            inp[p_c] += 1


    @classmethod
    def solution2(cls, inp: T) -> Any:
        pass