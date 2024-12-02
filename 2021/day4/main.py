import dataclasses
from collections import namedtuple
from typing import List, Dict, Any

import core as matrix
import core
import core as solution
from core import Matrix

Coordinate = namedtuple("Coordinate", "x y")


class BingoMatrix(Matrix):

    def __init__(self, rows: List[List[int]] = None):
        super().__init__(rows)
        self._mapped_values = self._map_values_to_coordinates(self._inner_data)
        self._rows_counters = self._init_row_counters(self._inner_data[0])
        self._cols_counters = self._init_row_counters(self._inner_data)

    @classmethod
    def _map_values_to_coordinates(cls, rows: List[List[int]]) -> Dict[int, Coordinate]:
        return {val: Coordinate(x=x, y=y) for y, row in enumerate(rows) for x, val in enumerate(row)}

    @classmethod
    def _init_row_counters(cls, lst: List[Any]) -> List[int]:
        return [len(lst) for _ in range(len(lst))]

    def mark_value(self, val: int) -> bool:
        if not (coordinate := self._mapped_values.pop(val, None)):
            return False

        row_vals = self._rows_counters[coordinate.x] - 1
        self._rows_counters[coordinate.x] = row_vals

        col_vals = self._cols_counters[coordinate.y] - 1
        self._rows_counters[coordinate.x] = c_vals

        return row_vals == 0


@dataclasses.dataclass
class InputState:
    numbers: [int]
    boards: [Matrix]


class Day4(solution.Solution):
    __day__ = 4

    @classmethod
    def read_input(cls, in_str: str) -> InputState:
        play_line_str, *matrices_str = in_str
        plays = core.parse.parse_int_lst(play_line_str, ",")
        matrices = matrix.create_matrices(matrices_str)
        return InputState(plays, matrices)

    @classmethod
    def solution1(cls, inp: InputState):
        pass

    @classmethod
    def solution2(cls, inp):
        return 44
