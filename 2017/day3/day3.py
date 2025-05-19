import dataclasses

import core.python.solution as solution

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
DIRECTIONS_DIAGONALS = DIRECTIONS + [(1, 1), (1, -1), (-1, 1), (-1, -1)]


@dataclasses.dataclass
class State:
    coordinate_at = (0, 0)
    current_direction = (1, 0)
    steps_in_direction = 1
    stepped_in_direction = 0

    def update(self):
        if self.steps_in_direction == self.stepped_in_direction:
            if abs(self.current_direction[1]) == 1:
                self.steps_in_direction += 1
            self.stepped_in_direction = 0
            self.current_direction = next_direction(self.current_direction)

        self.coordinate_at = add_tuples(self.coordinate_at, self.current_direction)
        self.stepped_in_direction += 1


def next_direction(current_direction: tuple[int, int]) -> tuple[int, int]:
    i = DIRECTIONS.index(current_direction)
    if i + 1 == len(DIRECTIONS):
        return DIRECTIONS[0]
    return DIRECTIONS[i + 1]


def add_tuples(tuple1: tuple[int, int], tuple2: [int, int]) -> tuple[int, int]:
    return tuple1[0] + tuple2[0], tuple1[1] + tuple2[1]


class Day1(solution.Solution):
    @classmethod
    def read_input(cls, lines: [str]) -> int:
        return int(lines[0])

    @classmethod
    def solution1(cls, inp: int) -> int:
        state = State()
        for i in range(inp - 1):
            state.update()
        return abs(state.coordinate_at[0]) + abs(state.coordinate_at[1])

    @classmethod
    def solution2(cls, inp: int) -> int:
        state = State()
        coordinate_vals = {(0, 0): 1}
        while True:
            state.update()
            check_directions = [add_tuples(state.coordinate_at, dr) for dr in DIRECTIONS_DIAGONALS]
            new_val = sum(map(lambda coord: coordinate_vals.get(coord, 0), check_directions))
            if new_val > inp:
                return new_val
            coordinate_vals[state.coordinate_at] = new_val
