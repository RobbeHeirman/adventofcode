from functools import partial
from typing import Iterable

from core.parse import to_grouped_lists
from core.solution import Solution

MirrorField = list[str]


def recursive_center_check(mirror_field: MirrorField, smudge_count: int, i: int, c: int) -> bool:
    if i - c < 0 or i + c + 1 >= len(mirror_field):
        return not smudge_count

    difference = map(lambda entry: entry[0] != entry[1], zip(mirror_field[i - c], mirror_field[i + c + 1]))
    smudges = sum(difference)

    if smudges > 1 or smudges == 1 and smudge_count == 0:
        return False

    if smudges == 1:
        smudge_count -= 1

    return recursive_center_check(mirror_field, smudge_count, i, c + 1)


def check_center(mirror_field: MirrorField, smudge_count, i: int) -> bool:
    if i + 1 == len(mirror_field):
        return False
    return recursive_center_check(mirror_field, smudge_count, i, 0)


def solve_mirror_field(mirror_field: MirrorField, smudge_count) -> int:
    checked = list(map(partial(check_center, mirror_field, smudge_count), range(len(mirror_field))))
    try:
        return checked.index(True) + 1
    except ValueError:
        return 0


def column_to_string(inp: list[str], column: int):
    return "".join(map(lambda row: row[column], inp))


def transpose(inp: list[str]) -> list[str]:
    return list(map(partial(column_to_string, inp), range(len(inp[0]))))


def get_matrix_value(smudge_count: int, matrix: MirrorField) -> int:
    horizontal = solve_mirror_field(matrix, smudge_count) * 100
    if horizontal:
        return horizontal

    transposed = transpose(matrix)
    return solve_mirror_field(transposed, smudge_count)


def solution(inp: Iterable[MirrorField], smudge_count: int) -> int:
    return sum(map(partial(get_matrix_value, smudge_count), inp))


class Day13(Solution):
    @classmethod
    def solution1(cls, inp: Iterable[MirrorField]) -> int:
        return solution(inp, 0)

    @classmethod
    def solution2(cls, inp: Iterable[MirrorField]) -> int:
        return solution(inp, 1)

    @classmethod
    def read_input(cls, lines: [str]) -> Iterable[MirrorField]:
        return to_grouped_lists(lines)
