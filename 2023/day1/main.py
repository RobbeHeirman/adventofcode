import functools
from typing import Iterable

from core import Solution

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


def replace_number_word_at_i(number_array_index: int, letter_of_word_index: int, input_string: str) -> str:
    """
    Replace a specific word on input_string at position i with the integer char value of input string.
    """
    i = letter_of_word_index
    k = number_array_index
    letter_word = WRITTEN_NUMBERS[k]

    if input_string[i: i + len(letter_word)] == letter_word:
        input_string = f"{input_string[:i]}{k + 1}{input_string[i + len(letter_word):]}"
    return input_string


def replace_for_number_words_at_i(input_string: str, i: int) -> str:
    """
    starting at index i of input string. try to replace number words with their integer vals as char.
    :return:
    """
    return functools.reduce(
        lambda accumulate, index: replace_number_word_at_i(index, i, accumulate),
        range(len(WRITTEN_NUMBERS)),
        input_string)


def replace_first_occurence(input_str: str) -> str:
    indices = map(lambda s: input_str.find(s), input_str)

    word_place = -1
    min_indice = len(input_str)
    for i, indice in enumerate(indices):
        if indice != -1 and indice < min_indice:
            word_place = i
            min_indice = indice


def words_to_integers(input_string: str) -> str:
    """
    takes a string and replaces all words spelled as integer into it with the integer string literals.
    """
    return functools.reduce(replace_for_number_words_at_i, range(len(input_string)), input_string)


def _to_first_and_last(line: str) -> str:
    """
    takes a string and return the first and last integer character concatenated.
    """
    numbs = list(filter(lambda letter: letter.isdigit(), line))
    return f"{numbs[0]}{numbs[-1]}"


def concatenate_first_and_last(lines: Iterable[str]) -> [str]:
    """
    given an iterable of strings.
    find the first and the last integer character in the string concatenated.
    """
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
        return cls.solution1(replaced_words)
