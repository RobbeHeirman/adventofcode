from dataclasses import dataclass
from functools import cache

import core.parse as parse
from core.solution import Solution


@dataclass(frozen=True)
class SpringRow:
    springs: str
    counted_broken: tuple[int, ...]


def line_to_spring_row(line: str) -> SpringRow:
    springs, spring_counts = line.split()
    spring_counts = parse.to_int_list(spring_counts, ",")
    return SpringRow(springs, tuple(spring_counts))


def unfold_spring_row(spring_row: SpringRow) -> SpringRow:
    five_it = (f"{spring_row.springs}?" * 5)
    inp_five = spring_row.counted_broken * 5
    return SpringRow(five_it[:-1], inp_five)


@cache
def solve_row(row: SpringRow) -> int:
    """
    Solve dynamic
    """
    springs = row.springs
    counts = row.counted_broken
    # We have no remaining subgroups left. One solution for all remaining ? are to be .
    # And we have no known broken springs left
    if not counts:
        return "#" not in springs
    current_count = counts[0]

    # Working springs at beginning and end don't matter
    springs = springs.strip(".")
    springs = springs.rstrip(".")

    # No solution if our spring string is smaller then the amount of broken springs needed in current group
    if len(springs) < current_count:
        return 0

    # Our spring string is empty we better matched all our group counts... otherwise this is not a solution
    if not springs:
        return int(not counts)

    # If first char is a ? we replace it with . or # and solve for that string.
    if springs[0] == "?":
        remove_first = springs[1:]
        return solve_row(SpringRow(remove_first, counts)) + solve_row(SpringRow('#' + remove_first, counts))

    sub_spring_str = springs[:current_count]
    # if there is a working spring between now and current count this cant be a solution
    if "." in sub_spring_str:
        return 0
    # if after the count group there is a broken spring again we cannot separate so this is not a solution
    if not current_count == len(springs) and springs[current_count] == "#":
        return 0
    # What remains are # or ?. We can just fill ? with # to match our number so this could be a valid
    # solution for this group count. Match the remaining string and groups.
    # the +1 is implicitly we say that current_count = ? or ., checked before and if ? is replaced by .
    return solve_row(SpringRow(springs[current_count + 1:], counts[1:]))


class Day12(Solution):
    @classmethod
    def read_input(cls, lines: [str]) -> [SpringRow]:
        return list(map(line_to_spring_row, lines))

    @classmethod
    def solution1(cls, inp: [SpringRow]) -> int:
        return sum(map(solve_row, tuple(inp)))

    @classmethod
    def solution2(cls, inp: [SpringRow]) -> int:
        rows = list(map(unfold_spring_row, inp))
        return cls.solution1(rows)
