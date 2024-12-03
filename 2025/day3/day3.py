from typing import Any
import re
from core.python.solution import Solution, T


class Day3(Solution):
    @classmethod
    def read_input(cls, lines: [str]) -> str:
        return "".join(lines)

    @classmethod
    def solution1(cls, inp: str) -> int:
        return sum(int(x[0]) * int(x[1]) for x in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", inp))

    @classmethod
    def solution2(cls, inp: str) -> int:
        enabled = True
        total = 0
        for a, b, do, dont in re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", inp):
            if do:
                enabled = True
            elif dont:
                enabled = False
            else:
                total += int(a)*int(b)*enabled
        return total
