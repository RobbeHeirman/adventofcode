import dataclasses
import queue
from typing import Optional, Union


class Grid:
    def __init__(self):
        self.grid = []

    def __getitem__(self, item):
        return self.grid[item]

    def item_of_path(self, path: 'Path') -> int:
        i, j = path.path_position
        return self.grid[i][j]

    def get_check_val(self, i: Union['Path', int], j: Optional[int] = None) -> int:
        if j is None:
            i, j = i.path_position

        val = self[i][j]
        if val == ord('E'):
            return ord('z')
        if val == ord('S'):
            return ord('a')
        return val

    def add_row(self, str_line: str) -> None:

        self.grid.append([ord(char) for char in str_line])

    def find_start(self) -> (int, int):
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if cell == ord('E'):
                    return i, j

    def row_size(self) -> int:
        return len(self.grid)

    def col_size(self) -> int:
        try:
            return len(self.grid[0])
        except IndexError:
            return 0


def parse_input(filename: str) -> Grid:
    grid = Grid()
    with open(filename) as f:
        for line in f.read().splitlines():
            grid.add_row(line)

    return grid


@dataclasses.dataclass
class Path:
    path_position: (int, int)
    path_counter: int = 0


def dfs(grid: Grid) -> int:
    # DFS with queue implementation
    expand_queue = queue.Queue()
    root_path = Path(grid.find_start())
    expand_queue.put(root_path)

    # Bookkeep visited nodes
    visited_nodes = {root_path.path_position}

    # Neighbour array
    neighbour_indexes = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    while not expand_queue.empty():
        path = expand_queue.get()
        # Stop condition:
        if grid.item_of_path(path) == ord('a'):
            return path.path_counter

        for neighbour in neighbour_indexes:
            ni = path.path_position[0] + neighbour[0]
            nj = path.path_position[1] + neighbour[1]

            # Boundary check
            if ni < 0 or ni >= grid.row_size() or nj < 0 or nj >= grid.col_size():
                continue

            # visited check
            if (ni, nj) in visited_nodes:
                continue

            # Can we climb check
            check_val = grid.get_check_val(path)
            neighbour_check_val = grid.get_check_val(ni, nj)

            if (check_val - neighbour_check_val) <= 1:
                nw_path = Path((ni, nj), path.path_counter + 1)
                expand_queue.put(nw_path)
                visited_nodes.add(nw_path.path_position)

def main():
    grid = parse_input('input.txt')
    print(dfs(grid))


if __name__ == '__main__':
    main()
