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
        empty_spaces = 0
        for row in self:
            if row.count(self.ROCK_SYMBOL):
                break
            empty_spaces += 1
        return len(self.grid) - empty_spaces

    @staticmethod
    def _create_rows_for_rock(rock_height):
        def inner_decorator(function):
            @functools.wraps(function)
            def wrapper(self: "Grid", *args, **kwargs):
                highest_row = self._find_highest_row()
                extra_rows = (self.EXTRA_SPAWN_HEIGHT - highest_row) + rock_height
                if extra_rows > 0:
                    self.grid.extend([[self.EMPTY_SYMBOL for _ in range(self.width)] for _ in range(extra_rows)])
                if extra_rows < 0:
                    for _ in range(abs(extra_rows)):
                        self.grid.pop()

                return function(self, *args, **kwargs)

            return wrapper

        return inner_decorator

    def _find_highest_row(self) -> int:
        for i, row in enumerate(self):
            if row.count(self.ROCK_SYMBOL):
                return i
        return len(self.grid)

    def create_rock_at_cell(self, row_index: int, col_index: int):
        self.active_cells.add((col_index, row_index))
        self[row_index][col_index] = self.ROCK_SYMBOL
        return self

    def _create_horizontal_line(self, row_index: int, length=3) -> "Grid":
        for i in range(self.SIDE_OFFSET, self.SIDE_OFFSET + length):
            self.create_rock_at_cell(row_index, i)
        return self

    def _create_vertical_line(self, col_index: int, height=3) -> "Grid":
        for i in range(height):
            self.create_rock_at_cell(i, col_index)
        return self

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
        self.active_cells = set()
        return spawners[rocks_spawned % len(spawners)]()

    def can_move_rock_down(self) -> bool:
        if not self.active_cells:
            return False

        for cell in self.active_cells:
            x, y = cell
            if y == len(self.grid) - 1 or (self[y + 1][x] == self.ROCK_SYMBOL and (x, y + 1) not in self.active_cells):
                return False

        return True

    def can_move_rock_sideways(self, right: int) -> bool:
        for cell in self.active_cells:
            x, y = cell
            if self.width <= x + right or x + right < 0:
                return False
            if self[y][x + right] == self.ROCK_SYMBOL and (x + right, y) not in self.active_cells:
                return False
        return True

    def move_active_rock(self, direction: tuple[int, int]) -> bool:
        if direction[1] == 1 and not self.can_move_rock_down():
            return False

        if direction[0] != 0 and not self.can_move_rock_sideways(direction[0]):
            return False

        right, down = direction
        new_active_cells = set()
        for cell in self.active_cells:
            x, y = cell
            new_x, new_y = (x + right, y + down)
            if (x, y) not in new_active_cells:
                self[y][x] = self.EMPTY_SYMBOL
            self[new_y][new_x] = self.ROCK_SYMBOL
            new_active_cells.add((new_x, new_y))
        self.active_cells = new_active_cells
        return True

    def get_top_row_indices(self):
        if not len(self):
            return [0 for _ in range(self.width)]

        end_condition = 2 ** self.width - 1
        top_rock_found = 0

        ret = []
        row_index = 0

        while end_condition != top_rock_found:
            if row_index == len(self):
                return ret
            row = self[row_index]
            bit_row = sum([(row[i] == self.ROCK_SYMBOL) << i for i in range(len(row))])
            ret.append(bit_row)
            top_rock_found = top_rock_found | bit_row
            row_index += 1
        return ret

    def solve(self, jetstream: str, rocks: int) -> int:
        jet_index = 0
        rock_spawn_counter = 0
        states = set()
        rock_count = {}
        height_count = {}
        extra_length = 0
        while True:
            if not self.can_move_rock_down():
                if rock_spawn_counter == rocks:
                    return len(self) + extra_length

                indices = self.get_top_row_indices()
                indices.append(jet_index % len(jetstream))
                indices.append(rock_spawn_counter % 5)
                indices = tuple(indices)

                if indices in states:
                    qty_rocks_in_rep = rock_spawn_counter - rock_count[indices]
                    repetition_length = len(self) - height_count[indices]
                    rocks_to_fall = rocks - rock_count[indices]
                    reps_in_rocks_to_fall = rocks_to_fall // qty_rocks_in_rep
                    rock_spawn_counter = qty_rocks_in_rep * reps_in_rocks_to_fall + rock_count[indices]
                    extra_length += reps_in_rocks_to_fall * repetition_length - repetition_length
                else:
                    states.add(indices)
                    rock_count[indices] = rock_spawn_counter
                    height_count[indices] = len(self)

                self.spawn_rock(rock_spawn_counter)
                rock_spawn_counter += 1
                # print("spawn")
                # print(self)
            else:
                self.move_active_rock((0, 1))
                # print('v')
                # print(self)

            curr_jet = jetstream[jet_index % len(jetstream)]
            right = -1 if curr_jet == "<" else 1 if curr_jet == ">" else 0
            if right == 0:
                continue
            self.move_active_rock((right, 0))
            jet_index += 1

        return len(self.grid) + extra_length


def main():
    pass
    grid = Grid()
    with open('input.txt') as f:
        jetstream = f.read().rstrip()
    grid.get_top_row_indices()
    print(grid.solve(jetstream, 1000000000000))


main()
