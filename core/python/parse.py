import itertools
from typing import Iterable


def to_int_list(inp: str, seperator=",") -> [int]:
    splits = inp.split(seperator)
    splits = filter(lambda x: x, splits)
    return list(map(lambda x: int(x), splits))


def to_grouped_lists(inp: [str], seperator="") -> list[list[str]]:
    groups = filter(lambda tup: not tup[0], itertools.groupby(inp, lambda line: line == seperator))
    groups = map(lambda group: list(group[1]), groups)
    return list(groups)


def parse_int_lst(in_str: str, seperator="\n") -> [int]:
    """
    Takes strings like
    '
    1
    2
    4
    5
    ...
    And converts this to [1, 2, 4, 5]
    '
    """
    return list(map(lambda x: int(x), in_str.split(seperator)))
