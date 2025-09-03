from collections.abc import Callable
from typing import Any, Protocol

from core.python.solution import Solution, T


class Signal(Protocol):
    def get_signal(self, wires: dict[str, "Signal"]) -> int:
        pass


def convert_to_constant(operand: str, wires: dict[str, Signal]) -> int:
    try:
        return int(operand)
    except ValueError:
        return wires[operand].get_signal(wires)


class OneOperandSignal(Protocol):
    def __init__(self, operand: str | int, operation: Callable[[int], int]):
        self._operand = operand
        self._operation = operation
        self._calculated_signal: int | None = None


    def get_signal(self, wires: dict[str, Signal]) -> int:
        if self._calculated_signal is None:
            in_signal = convert_to_constant(self._operand, wires)
            self._calculated_signal = self._operation(in_signal)
        return self._calculated_signal


class TwoOperationSignal:
    def __init__(self, operand1: str | int, operand2: str | int, opt: Callable[[int, int], int]):
        self._operand1 = operand1
        self._operand2 = operand2
        self._opt = opt

        self._calculated_signal: int | None = None

    def get_signal(self, wires: dict[str, Signal]) -> int:
        if self._calculated_signal is None:
            s1 = convert_to_constant(self._operand1, wires)
            s2 = convert_to_constant(self._operand2, wires)
            self._calculated_signal = self._opt(s1, s2)
        return self._calculated_signal


class Day7(Solution):
    @classmethod
    def read_input(cls, lines: list[str]) -> dict[str, Signal]:
        wires = {}
        no_op = lambda x: x
        negate_op = lambda x: ~x
        or_op = lambda x, y: x | y
        and_op = lambda x, y: x & y
        shift_left = lambda x, y: x << y
        shift_right = lambda x, y: x >> y

        for line in lines:
            splits = line.split(" ")
            if splits[1] == "->":
                constant = splits[0]
                wire = splits[2]
                wires[wire] = OneOperandSignal(constant, no_op)
                continue

            if splits[0] == "NOT":
                wire = splits[3]
                to_negate = splits[1]
                wires[wire] = OneOperandSignal(to_negate, negate_op)
                continue

            s1 = splits[0]
            s2 = splits[2]
            keyword = splits[1]
            wire = splits[4]

            if keyword == "AND":
                wires[wire] = TwoOperationSignal(s1, s2, and_op)
            elif keyword == "OR":
                wires[wire] = TwoOperationSignal(s1, s2, or_op)
            elif keyword == "LSHIFT":
                wires[wire] = TwoOperationSignal(s1, s2, shift_left)
            elif keyword == "RSHIFT":
                wires[wire] = TwoOperationSignal(s1, s2, shift_right)
        print(type(wires))
        return wires

    @classmethod
    def solution1(cls, wires: dict[str, Signal]) -> Any:
        return wires["a"].get_signal(wires)

    @classmethod
    def solution2(cls, inp: T) -> Any:
        return "?"
