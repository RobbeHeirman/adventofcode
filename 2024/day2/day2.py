from core.python.solution import Solution


def list_is_safe(lst: list) -> bool:
    asc_lst = sorted(lst)
    desc_lst = sorted(lst, reverse=True)

    if lst != asc_lst and desc_lst != lst:
        return False

    return all(1 <= abs(x[0] - x[1]) <= 3 for x in zip(lst, lst[1:]))


def with_adapted_sequence(lst: list[int]) -> bool:
    lsts = [lst[:i] + lst[i + 1:] for i in range(len(lst))]
    return any(map(list_is_safe, lsts))


class Day2(Solution):
    @classmethod
    def read_input(cls, lines: [str]) -> list[list[int]]:
        return [[int(x) for x in splitted_line.split()] for splitted_line in lines]

    @classmethod
    def solution1(cls, inp: list[list[int]]) -> int:
        return sum(map(list_is_safe, inp))

    @classmethod
    def solution2(cls, inp: list[list[int]]) -> int:
        return sum(map(with_adapted_sequence, inp))
