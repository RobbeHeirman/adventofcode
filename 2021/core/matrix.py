from typing import List
import itertools

class Matrix:
    @classmethod
    def create_matrix(cls, in_str: [str], seperator=" "):
        for line in in_str:
            int_line = map(lambda x: int(x), line.splitlines(seperator))
        grouped = [list(group) for l, group in itertools.groupby(in_str, lambda lst: lst == "") if ]
        print(grouped)

    def __init__(self, rows: List[List[int]] | None = None):
        self._inner_data = rows
