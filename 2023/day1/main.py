import functools

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


def _replace_for_word(number_array_index, letter_of_word_index, input_string):
    i = letter_of_word_index
    k = number_array_index
    letter_word = WRITTEN_NUMBERS[k]

    if input_string[i: i + len(letter_word)] == letter_word:
        input_string = f"{input_string[:i]}{k + 1}{input_string[i + len(letter_word):]}"
    return input_string


def _reduce_for_word_at_i(input_string, i):
    return functools.reduce(
        lambda accumulate, index: _replace_for_word(index, i, accumulate),
        range(len(WRITTEN_NUMBERS)),
        input_string)


def words_to_integers(input_string: str):
    return functools.reduce(_reduce_for_word_at_i, range(len(input_string)), input_string)


def _to_first_and_last(line: str):
    numbs = list(filter(lambda letter: letter.isdigit(), line))
    return numbs[0] + numbs[-1]


def concatenate_first_and_last(lines):
    return list(map(_to_first_and_last, lines))


class Day1(Solution):

    @classmethod
    def read_input(cls, lines: [str]) -> [str]:
        return lines

    @classmethod
    def solution1(cls, inp: [str]):
        concatenated = concatenate_first_and_last(inp)
        return sum(map(lambda x: int(x), concatenated))

    @classmethod
    def solution2(cls, inp: [str]):
        replaced_words = [words_to_integers(st) for st in inp]
        concatenated = concatenate_first_and_last(replaced_words)
        return sum(map(lambda x: int(x), concatenated))
