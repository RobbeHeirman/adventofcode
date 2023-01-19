import abc
import copy
import dataclasses
import enum
from typing import List, Optional


class Direction(enum.Enum):
    UP = 'U'
    DOWN = 'D'
    LEFT = 'L'
    RIGHT = 'R'


@dataclasses.dataclass(init=False)
class Movement:
    steps: int
    direction: Direction

    def __init__(self, in_str: str):
        # in_str example: D 2
        in_lst = in_str.split(' ')
        self.direction = Direction(in_lst[0])
        self.steps = int(in_lst[1])


class Coordinate(abc.ABC):
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y
        self._prev_coordinate: Optional['Coordinate'] = None
        self.subscribers: List[Coordinate] = []

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        prev__coordinate = self._prev_coordinate
        while prev__coordinate:
            yield prev__coordinate
            prev__coordinate = prev__coordinate._prev_coordinate

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    @abc.abstractmethod
    def update(self):
        pass

    @property
    def prev_coordinate(self):
        return self._prev_coordinate

    @prev_coordinate.setter
    def prev_coordinate(self, val: 'Coordinate'):
        self._prev_coordinate = copy.copy(val)

    def add_subscribe(self, subs: 'Coordinate') -> None:
        self.subscribers.append(subs)

    def update_subscribers(self) -> None:
        for subscriber in self.subscribers:
            subscriber.update()


class Head(Coordinate):

    def __init__(self):
        super().__init__()

    def move_direction(self, move: Movement) -> None:
        for _ in range(move.steps):
            self._move_step(move.direction)

    def _move_step(self, direction: Direction):
        self.prev_coordinate = self
        match direction:
            case Direction.UP:
                self.y += 1
            case Direction.DOWN:
                self.y -= 1
            case Direction.LEFT:
                self.x -= 1
            case Direction.RIGHT:
                self.x += 1
        self.update()

    def update(self):
        for sub in self.subscribers:
            sub.update()


class Tail(Coordinate):
    def __init__(self, head: Coordinate, x=0, y=0):
        super().__init__(x, y)
        self.head = head
        self.head.add_subscribe(self)

    def __str__(self):
        return f"HEAD: {self.head} TAIL{super().__str__()}"

    def __hash__(self):
        return hash((self.x, self.y))

    def update(self):
        self.prev_coordinate = self
        self.prev_coordinate.head = self.head
        self._update_step()

    def _update_step(self):
        # vertical check
        y_diff = self.head.y - self.y
        x_diff = self.head.x - self.x

        def _calc_replace(x: int):
            if x == 0:
                return 0
            return (abs(x) // 2) * (x // abs(x))

        # Same column
        if self.x == self.head.x:
            self.y += _calc_replace(y_diff)

        # same row
        elif self.y == self.head.y:
            self.x += _calc_replace(x_diff)

        else:
            # Diagonally
            if abs(y_diff) > 1 or abs(x_diff) > 1:
                self.y += 1 if y_diff > 0 else -1
                self.x += 1 if x_diff > 0 else -1

        self.update_subscribers()


def parse_input(filename):
    with open(filename) as f:
        return [Movement(line) for line in f.read().splitlines()]


def main():
    parsed_in = parse_input('input.txt')
    head = Head()
    tail_lst = [Tail(head)]

    for _ in range(8):
        tail = Tail(tail_lst[-1])
        tail_lst.append(tail)

    for move in parsed_in:
        head.move_direction(move)

    coord_lst = [coord for coord in tail_lst[-1]]

    #     print(coord)
    #
    print(len(set(coord_lst)))


if __name__ == '__main__':
    main()
