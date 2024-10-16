import functools
from typing import List, TypeVar, Type

import itertools

import core.parse as parse


class Matrix:
    def __init__(self, rows: List[List[int]] | None = None):
        self._inner_data = rows if rows is not None else []

    def __repr__(self):
        first_flatten = map(lambda row: "".join(str(row)), self._inner_data)
        return "\n" + "\n".join(first_flatten) + "\n"

    def add_row(self, row: List[int]) -> "Matrix":
        self._inner_data.append(row)
        return self


T = TypeVar("T", bound=Matrix)


def create_matrix(input_string_list: [str], seperator=" ", matrix_class: Type[T] = Matrix) -> T:
    """
    input_string_list expected to be:
    [
    "8 8 7 3",
    "7 2 1 3",
    "0 1 1 1"
    ]
    """
    return functools.reduce(
        lambda result_matrix, int_str: result_matrix.add_row(parse.to_int_list(int_str, seperator)),
        input_string_list,
        matrix_class()
    )


def create_matrices(input_string: List[str]):
    matrix_strings = [list(val) for key, val in itertools.groupby(input_string, lambda val: val == '') if not key]
    return list(map(lambda m: create_matrix(m, " "), matrix_strings))
