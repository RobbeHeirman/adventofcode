import dataclasses

import core.solution as solution
from core import input_parser
from core.matrix import Matrix


@dataclasses.dataclass
class State:
    numbers: [int]
    boards: [Matrix]


class Day4(solution.Solution):
    __day__ = 4

    @classmethod
    def read_input(cls, in_str: str):
        play_line_str, *matrices_str = in_str
        plays = input_parser.parse_int_lst(play_line_str, ",")
        matrices = Matrix.create_matrix(matrices_str)

    @classmethod
    def solution1(cls, inp):
        return 12

    @classmethod
    def solution2(cls, inp):
        return 44
