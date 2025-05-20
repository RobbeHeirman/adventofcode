import core.python.solution


def sum_matching_look_ahead(digits: list[int], look_ahead: int) -> int:
    return sum(
        map(lambda i: digits[i] if digits[i] == digits[(i + look_ahead) % len(digits)] else 0, range(len(digits))))


class Day1(core.python.solution.Solution):
    @classmethod
    def read_input(cls, lines: list[str]) -> list[int]:
        return [int(ch) for line in lines for ch in line]

    @classmethod
    def solution1(cls, digits: list[int]) -> int:
        return sum_matching_look_ahead(digits, 1)

    @classmethod
    def solution2(cls, digits: list[int]) -> int:
        halfway = len(digits) // 2
        return sum_matching_look_ahead(digits, halfway)

