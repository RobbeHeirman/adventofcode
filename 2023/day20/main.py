import re
from abc import abstractmethod, ABC
from collections import defaultdict
from dataclasses import dataclass
from enum import auto, Enum
from functools import partial
from itertools import chain
from operator import eq
from queue import Queue
from typing import Any

from core import foreach
from core import Solution


class Signal(Enum):
    LOW = auto()
    HIGH = auto()
    NONE = auto()


@dataclass(frozen=True)
class SignalState:
    source: "Module"
    state: Signal


class Module(ABC):
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name

    @abstractmethod
    def process_signal(self, signal_state: SignalState) -> SignalState:
        pass


class Broadcaster(Module):
    def process_signal(self, signal_state: SignalState) -> SignalState:
        return SignalState(self, Signal.LOW)


class FlipFlop(Module):
    def __init__(self, name: str):
        super().__init__(name)
        self._state = False

    def __repr__(self):
        return f"{self.name} {self._state}"

    def process_signal(self, signal_state: SignalState) -> SignalState:
        if signal_state.state == Signal.HIGH:
            return SignalState(self, Signal.NONE)

        self._state = not self._state
        signal = Signal.HIGH if self._state else Signal.LOW
        return SignalState(self, signal)


class Inverter(Module):
    def __init__(self, name: str, sources: list[str]):
        super().__init__(name)
        self._prev_state = dict(map(lambda s: (s, Signal.LOW), sources))

    def __repr__(self):
        return f"{self.name} {self._prev_state}"

    def process_signal(self, signal_state: SignalState) -> SignalState:
        self._prev_state[signal_state.source.name] = signal_state.state
        signal = Signal.HIGH if any(filter(partial(eq, Signal.LOW), self._prev_state.values())) else Signal.LOW
        return SignalState(self, signal)

class Output(Module):
    def __init__(self, name="output"):
        super().__init__(name)
        self._is_pressed = False

    def process_signal(self, signal_state: SignalState) -> SignalState:
        if signal_state.state == Signal.LOW:
            self._is_pressed = True

        return SignalState(self, Signal.NONE)

    def is_pressed(self) -> bool:
        return self._is_pressed


NAME_REGEX = re.compile(r"[a-z]+")


def get_source_target_names(inp: str) -> (str, list[str]):
    signal, target = inp.split("->")
    if not signal[0].isalpha():
        signal = signal[1:]
    signal = signal.strip()

    target = target.split(',')
    target = list(map(lambda t: t.strip(), target))
    return signal, target


def invert_dict_entry_entry(key: str, val: [str]) -> list[(str, str)]:
    return list(map(lambda ent: (ent, key), val))


def invert_list_dict(dct: dict[str, [str]]) -> dict[str, [str]]:
    inverted_entries = list(map(lambda ent: invert_dict_entry_entry(ent[0], ent[1]), dct.items()))
    dct = defaultdict(list)
    foreach(lambda ent: dct[ent[0]].append(ent[1]), chain(*inverted_entries))
    return dct


def module_factory(inverted_signals: dict[str, [str]], inp: str) -> Module:
    signal, target = get_source_target_names(inp)
    match inp[0]:
        case "b":
            return Broadcaster(signal)
        case "%":
            return FlipFlop(signal)
        case "&":
            return Inverter(signal, inverted_signals[signal])
        case _:
            raise NotImplementedError(signal)


def map_list_modules(in_lst: list[str], modules_mapped: dict[str, Module]) -> list[Module]:
    return list(map(lambda s: modules_mapped[s], in_lst))


def print_signal(old: SignalState, targets: list[Module]):
    for target in targets:
        print(f"{old.source.name}  -> {old.state.name} -> {target.name}")


@dataclass
class InputState:
    mapped_module_names: dict[str, Module]
    module_graph: dict[Module, [Module]]


def push_button(inp: "InputState", signal_counter: dict[Signal, int]):
    current_module = inp.mapped_module_names['broadcaster']
    graph = inp.module_graph
    signal_counter[Signal.LOW] += 1
    q = Queue()
    q.put(SignalState(current_module, Signal.LOW))
    while not q.empty():
        signal: SignalState = q.get()
        targets = graph[signal.source]

        signal_counter[signal.state] += len(targets)

        new_signals = list(map(lambda target: target.process_signal(signal), targets))
        new_signals = list(filter(lambda signal_state: signal_state.state != Signal.NONE, new_signals))
        foreach(lambda nw_signal: q.put(nw_signal), new_signals)


class Day20(Solution):

    @classmethod
    def read_input(cls, lines: [str]) -> InputState:
        source_target_dict = dict(map(get_source_target_names, lines))
        target_source_dict = invert_list_dict(source_target_dict)

        modules = list(map(partial(module_factory, target_source_dict), lines))
        modules.append(Output())

        modules_mapped = dict(map(lambda module: (module.name, module), modules))
        graph = dict(map(
            lambda entry: (modules_mapped[entry[0]], map_list_modules(entry[1], modules_mapped)),
            source_target_dict.items()
        ))
        return InputState(modules_mapped, graph)

    @classmethod
    def solution1(cls, inp: InputState) -> int:
        signal_counter = {
            Signal.LOW: 0,
            Signal.HIGH: 0
        }

        for _ in range(1000):
            push_button(inp, signal_counter)

        return signal_counter[Signal.LOW] * signal_counter[Signal.HIGH]

    @classmethod
    def solution2(cls, inp: InputState) -> Any:

        output: Output = inp.mapped_module_names['output']
        signal_counter = {
            Signal.LOW: 0,
            Signal.HIGH: 0
        }
        counter = 0
        while not output.is_pressed():
            push_button(inp, signal_counter)
            counter += 1
        return counter