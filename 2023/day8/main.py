import itertools
import re
from dataclasses import dataclass

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


class Day8(Solution):
    @classmethod
    def read_input(cls, lines: [str]) -> Input:
        walk_pattern, network_pattern = lines[:1], lines[2:]
        dct = dict(map(parse_line_to_entry, network_pattern))
        return Input(walk_pattern[0], dct)

    @classmethod
    def solution1(cls, inp: Input):
        cycler = itertools.cycle(inp.walk_pattern)
        current_room = "AAA"
        counter = 0
        while current_room != "ZZZ":
            counter += 1
            current_room = inp.network[current_room][next(cycler)]
        return counter

    @classmethod
    def solution2(cls, inp: Input):
        cycler = itertools.cycle(inp.walk_pattern)
        locs = list(filter(lambda ent: ent[2] == "A", inp.network.keys()))
        counter = 0
        print(locs)
        while not all(map(lambda room: room[2] == "Z", locs)):
            counter += 1
            direction = next(cycler)

            locs = list(map(lambda room: inp.network[room][direction], locs))
        return counter
