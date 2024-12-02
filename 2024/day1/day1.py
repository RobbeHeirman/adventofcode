from collections import Counter

from core.python.solution import Solution


class Day1(Solution):
    __filename__ = "input.txt"

    @classmethod
    def read_input(cls, lines: [str]) -> tuple[list[int], list[int]]:
        lst1 = [int(line.split()[0]) for line in lines]
        lst2 = [int(line.split()[1]) for line in lines]
        return lst1, lst2

    @classmethod
    def solution1(cls, inp: tuple[list[int], list[int]]) -> int:
        return sum(abs(x[0] - x[1]) for x in zip(sorted(inp[0]), sorted(inp[1])))


    @classmethod
    def solution2(cls, inp: tuple[list[int], list[int]]) -> int:
        counted = Counter(inp[1])
        return sum(x * counted.get(x, 0) for x in inp[0])
