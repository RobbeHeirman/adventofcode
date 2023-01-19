import abc
import dataclasses
from typing import List, Iterable, Dict, Tuple

StackType = Dict[int, List[str]]


@dataclasses.dataclass
class Move:
    amount: int
    begin: int
    to: int


class Parser:
    def __init__(self, filename: str):

        with open(filename) as file:
            self.__INIT_ROWS = self._make_init_rows(file)
            self.__MOVES = self._make_moves(file)

    @property
    def moves(self):
        return self.__MOVES

    @staticmethod
    def _make_init_rows(lines: Iterable[str]) -> List[List[Tuple[int, str]]]:
        stack_rows = []
        for line in lines:
            stck_row = [(i // 4, line[i + 1]) for i, chr_ in enumerate(line) if '[' in chr_]
            if not stck_row:  # early stop assume the init config starts and continues with the stacks drawn.
                break
            stack_rows.append(stck_row)
        return stack_rows

    @staticmethod
    def _make_moves(lines: Iterable[str]) -> List[Move]:
        moves = []
        for line in lines:
            split = line.split()
            try:
                if split[0] == 'move':
                    move = Move(amount=int(split[1]), begin=int(split[3]) - 1, to=int(split[5]) - 1)
                    moves.append(move)
            except IndexError:
                pass

        return moves

    def create_init_config(self) -> StackType:
        stacks = {}
        for stack_row in reversed(self.__INIT_ROWS):
            for box in stack_row:
                stack_num = box[0]
                box_letter = box[1]
                if q := stacks.get(stack_num, False):
                    q.append(box_letter)
                else:
                    stacks[stack_num] = [box_letter]
        return stacks


class Crane(abc.ABC):

    def solve(self, initial_state: StackType, moves) -> str:
        self._move_creates(initial_state, moves)
        return self._get_answer(initial_state)

    def _move_creates(self, stacks: StackType, moves: List[Move]):
        for move in moves:
            self._move_func(stacks, move)

    @abc.abstractmethod
    def _move_func(self, stacks: StackType, move: Move):
        pass

    @staticmethod
    def _get_answer(stacks: StackType) -> str:
        answer = ""
        for key in sorted(stacks1.keys()):
            try:
                answer += stacks[key][-1]
            except IndexError:  # Some lists can be empty
                pass
        return answer


class Crane9000(Crane):

    def _move_func(self, stacks: StackType, move: Move):
        from_queue = stacks[move.begin]
        to_queue = stacks[move.to]
        for _ in range(move.amount):
            box_ = from_queue.pop()
            to_queue.append(box_)


class Crane9001(Crane):

    def _move_func(self, stacks: StackType, move: Move):
        nw_lst = []
        from_queue = stacks[move.begin]
        to_queue = stacks[move.to]
        for _ in range(move.amount):
            box_ = from_queue.pop()
            nw_lst.append(box_)
        nw_lst.reverse()
        to_queue.extend(nw_lst)


if __name__ == '__main__':
    parser = Parser("../../../adventofcode/2022/day5.txt")
    stacks1 = parser.create_init_config()
    stacks2 = parser.create_init_config()

    crane1 = Crane9000()
    crane2 = Crane9001()

    print(crane1.solve(stacks1, parser.moves))
    print(crane2.solve(stacks2, parser.moves))
