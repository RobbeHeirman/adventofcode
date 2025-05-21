from abc import ABCMeta
from typing import Type

import core.python.solution as solution


class _SolutionMeta(ABCMeta):

    def __new__(mcs: Type["solution.Solution"], name, bases, *args, **kwargs):
        c = super().__new__(mcs, name, bases, *args, **kwargs)
        if not bases[0].__name__ == "Generic":
            mcs._print_solution(c)
        return c

    def _print_solution(cls: Type["solution.Solution"]):
        solvers = {
            "1": cls.solution1,
            "2": cls.solution2
        }
        lines = cls.read_file()
        inp = cls.read_input(lines)
        for key, val in solvers.items():
            print(f"Solution for {cls.__name__}, part {key} is {val(inp[:])}")
