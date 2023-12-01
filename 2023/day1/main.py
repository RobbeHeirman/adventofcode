import functools
from typing import Iterable

from core.solution import Solution

WRITTEN_NUMBERS = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]


def replace_number_word_at_i(number_array_index: str, letter_of_word_index: int, input_string: str) -> str:
    i = letter_of_word_index
    k = number_array_index
    letter_word = WRITTEN_NUMBERS[k]

    if input_string[i: i + len(letter_word)] == letter_word:
        input_string = f"{input_string[:i]}{k + 1}{input_string[i + len(letter_word):]}"
    return input_string


def replace_for_number_words_at_i(input_string: str, i: int) -> str:
    return functools.reduce(
        lambda accumulate, index: replace_number_word_at_i(index, i, accumulate),
        range(len(WRITTEN_NUMBERS)),
        input_string)


def words_to_integers(input_string: str) -> str:
    return functools.reduce(replace_for_number_words_at_i, range(len(input_string)), input_string)


def _to_first_and_last(line: str) -> str:
    numbs = list(filter(lambda letter: letter.isdigit(), line))
    return numbs[0] + numbs[-1]


def concatenate_first_and_last(lines: Iterable) -> [str]:
    return list(map(_to_first_and_last, lines))


class Day1(Solution):

    @classmethod
    def read_input(cls, lines: [str]) -> [str]:
        return lines

    @classmethod
    def solution1(cls, inp: [str]) -> int:
        concatenated = concatenate_first_and_last(inp)
        return sum(map(lambda x: int(x), concatenated))

    @classmethod
    def solution2(cls, inp: [str]) -> int:
        replaced_words = map(words_to_integers, inp)
        concatenated = concatenate_first_and_last(replaced_words)
        return sum(map(lambda x: int(x), concatenated))
