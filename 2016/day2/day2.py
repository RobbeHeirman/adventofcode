from typing import Any

from core.python.solution import Solution, T


class Day2(Solution):
    @classmethod
    def read_input(cls, lines: list[str]) -> T:
        last = [line.split('/')[-1] for line in lines[1:]]
        ids = [f'"{l.split("-")[-1]}"' for l in last]
        output = str.join(",\n", ids)
        with open("output.txt", "w") as f:
            f.write(output)
    @classmethod
    def solution1(cls, inp: T) -> Any:
        pass

    @classmethod
    def solution2(cls, inp: T) -> Any:
        pass