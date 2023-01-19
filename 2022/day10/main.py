import abc
from typing import List


class State:

    def __init__(self):
        self.x = 1


class Instruction(abc.ABC):

    def __init__(self, cycle_time):
        self.cycle_time = cycle_time

    def do_cycle(self, state: State) -> None:
        self.operation(state)

    @abc.abstractmethod
    def operation(self, state: State):
        pass

    def operation_done(self) -> bool:
        return self.cycle_time == 0


class NoopInstruction(Instruction):
    def __init__(self):
        super().__init__(1)

    def __str__(self):
        return f'NOOP'

    def operation(self, state: State):
        pass


class AddInstruction(Instruction):

    def __init__(self, val: float):
        super().__init__(2)
        self._val = val

    def __str__(self):
        return f'ADD {self._val}'

    def operation(self, state: State):
        state.x += self._val


def parse_instruction(file: str) -> List[Instruction]:
    ret = []
    with open(file) as f:
        for line in f.read().splitlines():
            lst_line = line.split(' ')

            instruction_str = lst_line[0]

            instruction: Instruction
            if instruction_str == 'addx':
                instruction = AddInstruction(float(lst_line[1]))
            else:
                instruction = NoopInstruction()

            ret.append(instruction)

    return ret


def main():
    instructions = parse_instruction('input.txt')
    signal_strenghts = []
    cycle_counter = 0

    state = State()

    ret_str = ''
    for instruction in instructions:
        for _ in range(instruction.cycle_time):
            if cycle_counter in [state.x -1, state.x, state.x + 1]:
                ret_str += '#'
            else:
                ret_str += '.'

            cycle_counter += 1
            if cycle_counter == 40:
                cycle_counter = 0
                print(ret_str)
                ret_str = ''
        instruction.do_cycle(state)

    print(sum(signal_strenghts))


if __name__ == '__main__':
    main()
