from itertools import count
from typing import Callable

import core.python.solution as solution


def simple_incrementer(pc: int, instructions: list[int]) -> None:
    instructions[pc] += 1


def by_3_incrementer(pc: int, instructions: list[int]) -> None:
    increment = 1 if instructions[pc] < 3 else -1
    instructions[pc] += increment


def solve(instructions: list[int], instruction_updater: Callable[[int, list[int]], None]) -> int:
    pc = 0
    for steps in count(1):
        instruction = instructions[pc]
        instruction_updater(pc, instructions)
        pc += instruction
        if pc >= len(instructions):
            return steps


class Day5(solution.Solution):
    @classmethod
    def read_input(cls, lines: [str]) -> list[int]:
        return [int(l) for l in lines]

    @classmethod
    def solution1(cls, inp: list[int]) -> int:
        return solve(inp, simple_incrementer)

    @classmethod
    def solution2(cls, inp: list[int]) -> int:
        return solve(inp, by_3_incrementer)
