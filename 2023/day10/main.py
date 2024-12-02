from collections import namedtuple
from enum import Enum

from core import Solution

Coordinate = namedtuple("coordinate", "i j")


class Direction(Enum):
    NORTH = (-1, 0)
    EAST = (0, 1)
    SOUTH = (1, 0)
    WEST = (0, -1)

    def get_next_coordinate(self, coord: Coordinate) -> Coordinate:
        i, j = self.value
        return Coordinate(coord.i + i, coord.j + j)


DIRECTION_TO_SYMBOLS = {
    Direction.NORTH: {"|", "L", "J"},
    Direction.EAST: {"L", "F", "-"},
    Direction.SOUTH: {"|", "7", "F"},
    Direction.WEST: {"-", "J", "7"}
}

CONNECTING_DIRECTION = {
    Direction.NORTH: Direction.SOUTH,
    Direction.EAST: Direction.WEST,
    Direction.SOUTH: Direction.NORTH,
    Direction.WEST: Direction.EAST
}

SYMBOLS_TO_DIRECTION = dict()
for k, v in DIRECTION_TO_SYMBOLS.items():
    for item in v:
        SYMBOLS_TO_DIRECTION.setdefault(item, set()).add(k)


def find_start(lines) -> Coordinate:
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "S":
                return Coordinate(i, j)


def find_start_symbol(coord: Coordinate, inp: [str]) -> str:
    possible_dirs = []
    for direction in Direction:
        direct_val = direction.value
        i, j = (coord.i + direct_val[0], coord.j + direct_val[1])

        if not 0 <= i < len(inp) and 0 <= j < len(inp[i]):
            continue
        symbol = inp[i][j]
        if symbol not in SYMBOLS_TO_DIRECTION.keys():
            continue

        dirs = SYMBOLS_TO_DIRECTION[symbol]
        inverse_this_dir = CONNECTING_DIRECTION[direction]
        if inverse_this_dir in dirs:
            possible_dirs.append(direction)

    potential_symbols = map(lambda dr: DIRECTION_TO_SYMBOLS[dr], possible_dirs)
    f_set = set.intersection(*potential_symbols)
    return f_set.pop()  # Assumption only one pipe fits on this spot


def find_loop(inp: [str]) -> [Coordinate]:
    inp = inp[:]
    start = find_start(inp)
    symbol = find_start_symbol(start, inp)
    inp[start.i] = inp[start.i].replace("S", symbol)

    direction1, _ = SYMBOLS_TO_DIRECTION[symbol]
    loc = direction1.get_next_coordinate(start)
    visited_locs = [loc]
    while loc != start:
        symbol = inp[loc.i][loc.j]
        next_direction = SYMBOLS_TO_DIRECTION[symbol]
        direction1 = [dr for dr in next_direction if CONNECTING_DIRECTION[dr] != direction1][0]
        loc = direction1.get_next_coordinate(loc)
        visited_locs.append(loc)
    return visited_locs


INNER_LOCATION = {
    Direction.NORTH: Direction.EAST,
    Direction.EAST: Direction.SOUTH,
    Direction.SOUTH: Direction.WEST,
    Direction.WEST: Direction.NORTH
}


def find_inner_coordinates(loop: [Coordinate]) -> [Coordinate]:
    result = set()
    for this_coordinate, next_coordinate in zip(loop, loop[1:] + [loop[0]]):
        direction = (next_coordinate.i - this_coordinate.i, next_coordinate.j - this_coordinate.j)
        inner_location_direction = INNER_LOCATION[Direction(direction)]
        i, j = inner_location_direction.value
        inner_direction = (this_coordinate.i + i, this_coordinate.j + j)
        result.add(inner_direction)
    return result


class Day10(Solution):
    @classmethod
    def read_input(cls, lines: [str]) -> [str]:
        return lines

    @classmethod
    def solution1(cls, inp: [str]):
        return len(find_loop(inp)) // 2

    @classmethod
    def solution2(cls, inp: T):
        looped = find_loop(inp)
        find_inner_coordinates(looped)
