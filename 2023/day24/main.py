from dataclasses import dataclass, field
from functools import partial
from typing import Any, Iterable

from core.solution import Solution, T


@dataclass
class Path:
    pos: tuple[int, int]
    positions_visited: set[tuple[int, int]] = field(default_factory=set)


@dataclass
class Vertice:
    source: int
    target: int
    cost: int


DIRECTIVE_MAPPING = {
    "<": (0, -1),
    "v": (1, 0),
    ">": (0, 1),
    "^": (-1, 0),
}


def add_tuples(tuple1: tuple[int, int], tuple2: tuple[int, int]) -> tuple[int, int]:
    return tuple1[0] + tuple2[0], tuple1[1] + tuple2[1]


def valid_direction(pos: tuple[int, int], inp: [str]) -> list[tuple[int, int]]:
    symbol = inp[pos[0]][pos[1]]
    dirs = DIRECTIVE_MAPPING.values() if symbol == "." else [DIRECTIVE_MAPPING[symbol]]

    neighbors = map(partial(add_tuples, pos), dirs)
    neighbors = filter(lambda neighbor: 0 <= neighbor[0] < len(inp), neighbors)
    neighbors = filter(lambda neighbor: 0 <= neighbor[1] < len(inp[pos[0]]), neighbors)
    neighbors = filter(lambda neighbor: inp[neighbor[0]][neighbor[1]] != '#', neighbors)
    return list(neighbors)


def create_graph(inp: [str]) -> dict[int, list[Vertice]]:
    start = inp[0].index(".")
    end = inp[-1].index(".")

    visited = set()
    to_expand = [(start, 0)]
    while to_expand:
        current, count = to_expand.pop()
        visited.add(current)

        neighbors = valid_direction(current, inp)
        if not neighbors:
            continue
        if len(neighbors) == 1:
            to_expand.append([(neighbors[0], count + 1)])
            continue
        

class Day24(Solution):
    __filename__ = "example.txt"

    @classmethod
    def read_input(cls, lines: [str]) -> T:
        return lines

    @classmethod
    def solution1(cls, inp: [str]) -> Any:
        # find starting position
        # Ending pos
        max_length = 0

        # to_expand = queue.Queue()
        # to_expand.put(Path((0, start)))
        # while to_expand:
        #     current_expand: Path = to_expand.get()
        #     current_pos = current_expand.pos
        #     current_path = current_expand.positions_visited
        #     for neighbor in valid_direction(current_pos, inp):
        #         if neighbor == end:
        #             max_length = max(max_length, len(current_path) + 1)
        #             continue
        #
        #         if neighbor in current_path:
        #             continue
        #
        #         symbol = inp[neighbor[0]][neighbor[1]]
        #         if symbol == "#":
        #             continue
        #
        #         nw_path = copy.copy(current_path)
        #         nw_path.add(neighbor)
        #         to_expand.put(Path(neighbor, nw_path))
        # return max_length

    @classmethod
    def solution2(cls, inp: T) -> Any:
        pass
