import dataclasses

import core.matrix as matrix
import core.solution as solution
from core import input_parser
from core.matrix import Matrix


@dataclasses.dataclass
class InputState:
    numbers: [int]
    boards: [Matrix]


class Day4(solution.Solution):
    __day__ = 4

    @classmethod
    def read_input(cls, in_str: str) -> InputState:
        play_line_str, *matrices_str = in_str
        plays = input_parser.parse_int_lst(play_line_str, ",")
        matrices = matrix.create_matrices(matrices_str)
        return InputState(plays, matrices)

    @classmethod
    def solution1(cls, inp: InputState):
        pass

    @classmethod
    def solution2(cls, inp):
        return 44
