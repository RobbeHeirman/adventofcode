import dataclasses
from typing import Any

from core.python.solution import Solution, T


@dataclasses.dataclass
class Register:
    registers: list[int]

    def redistribute(self) -> tuple[int, ...]:
        highest = 0
        index_highest = 0
        for i, val in enumerate(self.registers):
            if val > highest:
                highest = val
                index_highest = i

        self.registers[index_highest] = 0
        for i in range(highest):
            index_highest += 1
            if index_highest == len(self.registers):
                index_highest = 0
            self.registers[index_highest] += 1
        return tuple(self.registers)


class Day6(Solution):
    @classmethod
    def read_input(cls, lines: list[str]) -> T:
        return list(map(int, lines[0].split("\t")))

    @classmethod
    def solution1(cls, inp: T) -> Any:
        register = Register(inp)
        found_configs = set()
        while True:
            new = register.redistribute()
            if new in found_configs:
                return len(found_configs)
            found_configs.add(new)

    @classmethod
    def solution2(cls, inp: T) -> Any:
        pass
