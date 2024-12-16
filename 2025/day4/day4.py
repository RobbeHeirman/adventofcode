from typing import Any

from core.python.solution import Solution, T


class Day4(Solution):

    LETTERS = ["X", "M", "A", "S"]
    DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1), (1, 1)]

    @classmethod
    def look_in_direction(cls, inp: list[str], pos: tuple[int, int], direction: tuple[int, int]) -> bool:
        for k, letter in enumerate(cls.LETTERS):
            i = pos[0] + direction[0] * k
            j = pos[1] + direction[1] * k

            if i < 0 or i >= len(inp) or j < 0 or j >= len(inp[0]):
                return False
            if letter != inp[i][j]:
                return False
        return True

    @classmethod
    def handle_x(cls, inp, pos) -> bool:

        i, j = pos[0], pos[1]
        if inp[pos[0]][pos[1]] != "A":
            return False

        if pos[0] < 1 or pos[0] >= len(inp[0]) - 1 or pos[1] < 1 or pos[1] >= len(inp) - 1:
            return False

        dig_1 = {inp[i - 1][j - 1], inp[i + 1][j + 1]}
        dig_2 = {inp[i + 1][j - 1], inp[i - 1][j + 1]}
        if dig_1 != {"M", "S"} or dig_2 != {"M", "S"}:
            return False
        return True

    @classmethod
    def read_input(cls, lines: [str]) -> T:
        return lines

    @classmethod
    def solution1(cls, inp: T) -> int:
        total = 0
        for i in range(len(inp[0])):
            for j in range(len(inp)):
                for direction in cls.DIRECTIONS:
                    total += cls.look_in_direction(inp, (i, j), direction)

        return total

    @classmethod
    def solution2(cls, inp: T) -> Any:
        total = 0
        for i in range(len(inp)):
            for j in range(len(inp[0])):
                total += cls.handle_x(inp, (i, j))
        return total
