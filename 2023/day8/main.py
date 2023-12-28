import itertools
import math
import re
from dataclasses import dataclass
from typing import Callable

from core.solution import Solution

CAPITALS_REGEX = re.compile(r"([0-9A-Z]+)")


@dataclass
class Entry:
    left: str
    right: str

    def __getitem__(self, key):
        match key:
            case "L":
                return self.left
            case "R":
                return self.right
            case _:
                raise NotImplementedError(f"No option for {key}")


@dataclass
class Input:
    walk_pattern: str
    network: dict[str, Entry]


def parse_line_to_entry(line: str) -> (str, Entry):
    key, value = line.split("=")
    entry = Entry(*CAPITALS_REGEX.findall(value))
    return key.strip(), entry


@dataclass
class GhostPathInfo:
    length_to_end: int
    start_of_cycle: int
    cycle_length: int


def get_ghost_path_info(space: Input, start_room: str, end_condition: Callable[[str], bool]) -> GhostPathInfo:
    """
    This discovered that it was completely unnecessary to search for al those stats.
    """
    cycler = itertools.cycle(enumerate(space.walk_pattern))
    cycle = next(cycler)

    counter = 0
    loc = start_room

    discovered_rooms_movement_ordered = []
    discovered_rooms_movement_i = set()

    while (loc, cycle[0]) not in discovered_rooms_movement_i:
        discovered_rooms_movement_ordered.append((loc, cycle[0]))
        discovered_rooms_movement_i.add((loc, cycle[0]))
        counter += 1

        loc = space.network[loc][cycle[1]]
        cycle = next(cycler)

    end_rooms = list(map(lambda tup: end_condition(tup[0]), discovered_rooms_movement_ordered))
    length_first = end_rooms.index(True)
    cycle_start = discovered_rooms_movement_ordered.index((loc, cycle[0]))
    return GhostPathInfo(length_first,
                         cycle_start,
                         len(discovered_rooms_movement_ordered) - cycle_start
                         )


class Day8(Solution):
    @classmethod
    def read_input(cls, lines: [str]) -> Input:
        walk_pattern, network_pattern = lines[:1], lines[2:]
        dct = dict(map(parse_line_to_entry, network_pattern))
        return Input(walk_pattern[0], dct)

    @classmethod
    def solution1(cls, inp: Input):
        current_room = "AAA"
        return get_ghost_path_info(inp, current_room, lambda room: room == "ZZZ").length_to_end

    @classmethod
    def solution2(cls, inp: Input):
        locs = list(filter(lambda ent: ent[2] == "A", inp.network.keys()))
        lengths = map(lambda room: get_ghost_path_info(inp, room, lambda r: r[2] == "Z").length_to_end, locs)
        return math.lcm(*lengths)
