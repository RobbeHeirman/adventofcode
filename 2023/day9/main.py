import functools
from typing import Callable

from core import to_int_list
from core import Solution


def difference_lines(line: [int]) -> [[int]]:
    if sum(line) == 0:
        return [line]
    difference = list(map(lambda entry: entry[1] - entry[0], zip(line, line[1:])))
    return difference_lines(difference) + [line]


def line_solver(line: [int], reduce_func: Callable[[[int]], int]) -> int:
    return functools.reduce(reduce_func, difference_lines(line), 0)


class Day9(Solution):
    @classmethod
    def read_input(cls, lines: [str]) -> [int]:
        return list(map(lambda line: to_int_list(line, " "), lines))

    @classmethod
    def solution1(cls, inp: [int]) -> int:
        return sum(map(lambda line: line_solver(line, lambda acc, diff_line: acc + diff_line[-1]), inp))

    @classmethod
    def solution2(cls, inp: [int]) -> int:
        return sum(map(lambda line: line_solver(line, lambda acc, diff_line: diff_line[0] - acc), inp))
