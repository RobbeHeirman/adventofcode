from collections import Counter
from typing import Any

import core.python.solution as solution
from core.python.solution import T


class Day4(solution.Solution):
    @classmethod
    def read_input(cls, lines: list[str]) -> list[list[str]]:
        return list(map(lambda l: l.split(" "), lines))

    @classmethod
    def solution1(cls, inp: list[list[str]]) -> int:
        total = 0
        for phrase in inp:
            counter = Counter(phrase)
            total += not any(filter(lambda val: val > 1, counter.values()))
        return total
    @classmethod
    def solution2(cls, inp: list[list[str]]) -> int:
        total = 0
        for phrase in inp:
            anagrams = set()
            for word in phrase:
                sorted_word = "".join(sorted(word))
                if sorted_word in anagrams:
                    break
                anagrams.add(sorted_word)
            else:
                total += 1
        return total