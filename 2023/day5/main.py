from dataclasses import dataclass
from functools import partial
from itertools import groupby, chain
from operator import is_not
from typing import Union

from core import Solution


@dataclass
class Range:
    destination: int
    source: int
    length: int

    def is_in_source_range(self, num: int) -> bool:
        return self.source <= num <= self.source + self.length

    def map_to_destination(self, inp: int) -> int:
        return inp + (self.destination - self.source)

    def create_range_intersect(self, in_range: "Range") -> Union["Range", None]:
        dest1 = self.source + self.length
        dest2 = in_range.destination + in_range.length

        intersect_end = min(dest1, dest2)
        intersect_start = max(self.source, in_range.destination)

        diff_src_target = self.destination - self.source

        if intersect_end > intersect_start:
            return Range(
                intersect_start + diff_src_target,
                intersect_start,
                intersect_end - intersect_start
            )
        return None


@dataclass
class Map:
    source_name: str
    destination_name: str

    ranges: [Range]

    def map_to_dest_num(self, inp: int):
        try:
            first_range: Range = next(filter(lambda rng: rng.is_in_source_range(inp), self.ranges))
            return first_range.map_to_destination(inp)

        except StopIteration:
            return inp

    def map_range_to_dest_ranges(self, in_range: Range) -> [Range]:
        intersect_ranges = map(lambda rng: rng.create_range_intersect(in_range), self.ranges)
        intersect_ranges = filter(partial(is_not, None), intersect_ranges)
        intersect_ranges = list(sorted(intersect_ranges, key=lambda rang: -rang.source))
        if not intersect_ranges:
            return [in_range]

        # TODO: Fill in missing begin of range with source range

        # TODO: Fill in gaps with source range

        # TODO: Fill in missing end with source range.

        return intersect_ranges


@dataclass
class Input:
    seeds: [int]
    maps: [Map]


def str_to_ints(inp: str) -> [int]:
    return list(map(int, inp.split()))


def create_map(inp: [str]):
    filtered = list(filter(lambda x: x, inp))
    map_names = filtered[0].split()[0]
    source, dest = map_names.split("-to-")

    ranges = inp[1:]
    ranges = map(str_to_ints, ranges)
    ranges = list(map(lambda inp: Range(*inp), ranges))
    return Map(source, dest, ranges)


def recursive_map_seeds(current_map: Map, seeds: [int], map_dict: {str, Map}) -> [int]:
    new_seeds = list(map(lambda seed: current_map.map_to_dest_num(seed), seeds))
    if new_map := map_dict.get(current_map.destination_name, False):
        return recursive_map_seeds(new_map, new_seeds, map_dict)
    return new_seeds


def recursive_map_seeds_ranges(current_map: Map, seeds: [Range], map_dict: {str, Map}) -> [Range]:
    seeds = list(seeds)
    new_seeds = map(lambda seed: current_map.map_range_to_dest_ranges(seed), seeds)
    new_seeds = chain(*new_seeds)
    if new_map := map_dict.get(current_map.destination_name, False):
        return recursive_map_seeds_ranges(new_map, new_seeds, map_dict)
    return new_seeds


class Day5(Solution):
    @classmethod
    def read_input(cls, lines: [str]) -> Input:
        seeds = list(map(int, lines[0].split(":")[1].split()))
        remainder = lines[1:]

        groups = groupby(remainder, lambda line: line == '')
        groups = list(filter(lambda lst: lst != [""], map(lambda entry: list(entry[1]), groups)))
        maps = list(map(create_map, groups))
        return Input(seeds, maps)

    @classmethod
    def solution1(cls, inp: Input):
        map_dct = dict(map(lambda map: (map.source_name, map), inp.maps))
        start_map: Map = map_dct["seed"]
        seeds = recursive_map_seeds(start_map, inp.seeds, map_dct)
        return min(seeds)

    @classmethod
    def solution2(cls, inp: Input):
        map_dct = dict(map(lambda map: (map.source_name, map), inp.maps))
        start_map: Map = map_dct["seed"]
        seeds = inp.seeds
        in_ranges = list(map(
            lambda i: Range(seeds[i], 0, seeds[i + 1]),
            range(0, len(seeds), 2)
        ))
        seeds = recursive_map_seeds_ranges(start_map, in_ranges, map_dct)
        return min((map(lambda range: range.destination, seeds)))
