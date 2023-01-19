import functools


class Grid:
    ROCK_SYMBOL = "#"
    EMPTY_SYMBOL = '.'
    EXTRA_SPAWN_HEIGHT = 3
    SIDE_OFFSET = 2

    def __init__(self):
        self.grid: list[list[str]] = []
        self.active_cells: set[tuple[int, int]] = set()
        self.width = 7

    def __str__(self):
        return "\n".join([f'|{"".join(row)}|' for row in self]) + f"\n+{'-' * self.width}+"

    def __getitem__(self, item):
        return self.grid[-(item + 1)]

    def __iter__(self):
        return reversed(self.grid)

    def __len__(self):
        return len(self.grid)

    @staticmethod
    def _create_rows_for_rock(rock_height):
        def inner_decorator(function):
            @functools.wraps(function)
            def wrapper(self, *args, **kwargs):
                highest_row = self._find_highest_row()
                extra_rows = (self.EXTRA_SPAWN_HEIGHT - highest_row) + rock_height
                self.grid.extend([[self.EMPTY_SYMBOL for _ in range(self.width)] for _ in range(extra_rows)])
                return function(self, *args, **kwargs)

            return wrapper

        return inner_decorator

    def _find_highest_row(self) -> int:
        for i, row in enumerate(self):
            if row.count(self.ROCK_SYMBOL):
                return i
        return len(self.grid)

    def create_rock_at_cell(self, row_index: int, col_index: int):
        self.active_cells.add((row_index, col_index))
        self[row_index][col_index] = self.ROCK_SYMBOL
        return self

    def _create_horizontal_line(self, row_index: int, length=3) -> "Grid":
        for i in range(self.SIDE_OFFSET, self.SIDE_OFFSET + length):
            return self.create_rock_at_cell(row_index, i)

    def _create_vertical_line(self, col_index: int, height=3):
        for i in range(height):
            return self.create_rock_at_cell(i, col_index)

    @_create_rows_for_rock(rock_height=1)
    def spawn_minus_rock(self) -> "Grid":
        return self._create_horizontal_line(0, 4)

    @_create_rows_for_rock(rock_height=3)
    def spawn_plus_rock(self) -> "Grid":
        return self.create_rock_at_cell(0, self.SIDE_OFFSET + 1) \
            ._create_horizontal_line(1, 3) \
            .create_rock_at_cell(2, self.SIDE_OFFSET + 1)

    @_create_rows_for_rock(rock_height=3)
    def spawn_reverse_l(self) -> "Grid":
        return self._create_vertical_line(2 + 2, 2)._create_horizontal_line(2, 3)

    @_create_rows_for_rock(rock_height=4)
    def spawn_vertical_rock(self) -> "Grid":
        return self._create_vertical_line(2, 4)

    @_create_rows_for_rock(rock_height=2)
    def spawn_block_rock(self) -> "Grid":

        return self._create_horizontal_line(0, 2)._create_horizontal_line(1, 2)

    def spawn_rock(self, rocks_spawned: int):
        spawners = [self.spawn_minus_rock, self.spawn_plus_rock, self.spawn_reverse_l, self.spawn_vertical_rock,
                    self.spawn_block_rock]

        return spawners[rocks_spawned % len(spawners)]()

    def can_move_rock_down(self) -> bool:
        if not self.active_cells:
            return False

        for cell in self.active_cells:
            x, y = cell
            if y == len(self) - 1 or (self[x][y + 1] == self.ROCK_SYMBOL and (x, y + 1) not in self.active_cells):
                return False

        return True

    def can_move_rock_sideways(self, right: int) -> bool:
        for cell in self.active_cells:
            x, y = cell
            if self.width <= x + right < 0 or (
                    self[x][y + right] == self.ROCK_SYMBOL and (x, y + right) not in self.active_cells):
                return False

    def move_active_rock(self, direction: tuple[int, int]) -> bool:
        if not self.can_move_rock_down():
            return False

        right, down = direction
        new_active_cells = set()
        for cell in self.active_cells:
            x, y = cell
            new_x, new_y = (x + down, y + right)
            self[x][y] = self.EMPTY_SYMBOL
            self[new_x][new_y] = self.ROCK_SYMBOL
            new_active_cells.add((new_x, new_y))
        self.active_cells = new_active_cells
        return True

    def solve(self, jetstream: str, rocks: int) -> int:
        jet_index = 0
        rock_spawn_counter = 0
        while rock_spawn_counter <= rocks:
            if not self.can_move_rock_down():
                self.spawn_rock(rock_spawn_counter)
                rock_spawn_counter += 1
                print(self.grid)
            curr_jet = jetstream[jet_index % len(jetstream)]
            right = -1 if curr_jet == "<" else 1 if curr_jet == ">" else 0
            if right == 0:
                continue

            self.move_active_rock((0, 1))
            self.move_active_rock((right, 0))


        return len(self.grid)


def main():
    grid = Grid()
    with open('input.txt') as f:
        jetstream = f.read().rstrip()

    print(grid.solve(jetstream, 2022))
main()
