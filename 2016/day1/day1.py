import dataclasses
from typing import Any

from core.python.solution import Solution, T

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


@dataclasses.dataclass
class State:
    facing = DIRECTIONS[0]
    pos = (0, 0)

    def update(self, direction: str) -> list[tuple[int, int]]:
        rotation = direction[0]
        movement = int(direction[1:])
        self.facing = rotate(self.facing, rotation)
        result = [(self.pos[0] + self.facing[0] * i, self.pos[1] + self.facing[1] * i) for i in range(1, movement + 1)]
        self.pos = result[-1]
        return result

    def distance(self) -> int:
        return abs(self.pos[0]) + abs(self.pos[1])


def rotate(current_direction: tuple[int, int], direction: str) -> tuple[int, int]:
    i = DIRECTIONS.index(current_direction)
    i = i + 1 if direction == "R" else i - 1
    if i < 0:
        i = len(DIRECTIONS) - 1
    elif i == len(DIRECTIONS):
        i = 0

    return DIRECTIONS[i]


class Day1(Solution):

    @classmethod
    def read_input(cls, lines: list[str]) -> list[str]:
        return lines[0].split(", ")

    @classmethod
    def solution1(cls, inp: list[str]) -> int:
        state = State()
        for direction in inp:
            state.update(direction)
        return state.distance()

    @classmethod
    def solution2(cls, inp: list[str]) -> int:
        state = State()
        visited_pos = {(0, 0)}
        for direction in inp:
            next_pos = state.update(direction)
            for ps in next_pos:
                if ps in visited_pos:
                    return abs(ps[0]) + abs(ps[1])
                visited_pos.add(ps)
