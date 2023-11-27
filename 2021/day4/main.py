import dataclasses

import core.solution as solution


@dataclasses.dataclass
class Matrix:
    inner_matrix: [[int]]


@dataclasses.dataclass
class State:
    numbers: [int]
    boards: [Matrix]


class Day4(solution.Solution):
    __day__ = 4

    @classmethod
    def solution1(cls, inp):
        return 12

    @classmethod
    def solution2(cls, inp):
        return 44
