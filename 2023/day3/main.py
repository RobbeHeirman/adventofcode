import dataclasses
import functools
import itertools
import re
from typing import Iterable, Tuple

from core.solution import Solution, T

N_LOCS = list(filter(lambda tup: tup != (0, 0), itertools.product([-1, 0, 1], repeat=2)))
SPLIT_REGEX = re.compile(r'(\d+|[^0-9])')
SYMBOLS_REGEX = re.compile(r'[^\d.]')  # Regex overhead because im to lazy to look for all symbols in input.


@dataclasses.dataclass(frozen=True)
class Digit:
    num: int

    def __eq__(self, other):
        return self is other


def map_element(inp: str):
    if inp.isdigit():
        nw_digit = Digit(int(inp))
        return [nw_digit] * len(inp)
    return inp


def parse_row(inp: str):
    split = SPLIT_REGEX.findall(inp)
    mapped = map(map_element, split)
    return list(itertools.chain(*mapped))


def get_neighbouring_symbols(loc: (int, int), inp: [[str]]) -> Iterable[Tuple[int, int]]:
    i = loc[0]
    j = loc[1]
    locations_to_check = map(lambda tup: (i + tup[0], j + tup[1]), N_LOCS)
    locations_to_check = filter(lambda tup: 0 <= tup[0] < len(inp), locations_to_check)
    locations_to_check = filter(lambda tup: 0 <= tup[1] < len(inp[tup[0]]), locations_to_check)
    return map(lambda in_loc: inp[in_loc[0]][in_loc[1]], locations_to_check)


class Day3(Solution):
    @classmethod
    def read_input(cls, lines: [str]) -> [[str]]:
        return list(map(parse_row, lines))

    @classmethod
    def solution1(cls, inp: [[str]]):
        results = set()
        for i, row in enumerate(inp):
            for j, loc in enumerate(row):
                if isinstance(loc, Digit):
                    neighbouring_symbols = get_neighbouring_symbols((i, j), inp)
                    valid_symbols = filter(
                        lambda symbol: isinstance(symbol, str) and SYMBOLS_REGEX.fullmatch(symbol),
                        neighbouring_symbols
                    )
                    if any(valid_symbols):
                        results.add(loc)
        return sum(map(lambda digit: digit.num, results))

    @classmethod
    def solution2(cls, inp: T):
        result = []
        for i, row in enumerate(inp):
            for j, loc in enumerate(row):
                if loc == "*":
                    locations_to_check = get_neighbouring_symbols((i, j), inp)
                    valid_symbols = set(filter(lambda symbol: isinstance(symbol, Digit), locations_to_check))
                    if len(valid_symbols) == 2:
                        product = functools.reduce(lambda x, y: x.num * y.num, valid_symbols)
                        result.append(product)
        return sum(result)
