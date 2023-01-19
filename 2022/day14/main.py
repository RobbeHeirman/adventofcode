import enum
from typing import List, Tuple, Optional


class Tile(enum.Enum):
    AIR = '.'
    ROCK = '#'
    SAND = 'O'
    SAND_SOURCE = '+'


class Cave:
    SAND_SOURCE = (500, 0)

    def __init__(self):
        self._grid: List[List[Tile]] = [[Tile.AIR for _ in range(501)]]
        self.set_tile(Cave.SAND_SOURCE[0], Cave.SAND_SOURCE[1], Tile.SAND_SOURCE)
        self.can_grow_vertical = True

    def __str__(self):
        ret = ''
        for i, row in enumerate(self._grid):
            ret += f'{i}: '
            for cell in row:
                ret += '' + cell.value + ''
            ret += '\n'
        return ret

    def cave_extend(self, x: int, y: int) -> None:
        if len(self._grid) <= y:
            if self.can_grow_vertical:
                for _ in range(len(self._grid), y + 1):
                    self._grid.append([Tile.AIR])

        if len(self._grid[y]) <= x:
            for _ in range(len(self._grid[y]), x + 1):
                self._grid[y].append(Tile.AIR)

    def get_tile(self, x: int, y: int):
        self.cave_extend(x, y)
        return self._grid[y][x]

    def set_tile(self, x: int, y: int, tile: Tile, extend=True):
        if extend:
            self.cave_extend(x, y)
        self._grid[y][x] = tile

    def _add_vertical_row(self, x: int, y1: int, y2: int):
        low, high = tuple(sorted([y1, y2]))
        for i in range(low, high + 1):
            tile = Tile.ROCK
            self.set_tile(x, i, tile)

    def _add_horizontal_row(self, y: int, x1: int, x2: int):
        low, high = tuple(sorted([x1, x2]))
        for i in range(low, high + 1):
            tile = Tile.ROCK
            self.set_tile(i, y, tile)

    def add_rock_row(self, coord1: Tuple[int, int], coord2: Tuple[int, int]) -> 'Cave':
        if coord1[0] == coord2[0]:
            self._add_vertical_row(coord1[0], coord1[1], coord2[1])
        else:
            self._add_horizontal_row(coord1[1], coord1[0], coord2[0])
        return self

    def move_sand(self, sand_pos: Tuple[int, int]) -> Optional[Tuple[int, int]]:
        if sand_pos[1] + 1 >= len(self._grid):
            return None

        solids = [Tile.ROCK, Tile.SAND]
        if self.get_tile(sand_pos[0], sand_pos[1] + 1) not in solids:
            return sand_pos[0], sand_pos[1] + 1

        if sand_pos[0] > 0 and self.get_tile(sand_pos[0] - 1, sand_pos[1] + 1) not in solids:
            return sand_pos[0] - 1, sand_pos[1] + 1

        if self.get_tile(sand_pos[0] + 1, sand_pos[1] + 1) not in solids:
            return sand_pos[0] + 1, sand_pos[1] + 1

        return None

    def count_resting_sand(self) -> int:
        counter = 0
        self.can_grow_vertical = False
        self._grid.append([Tile.AIR])
        sand_piece = Cave.SAND_SOURCE

        while self.move_sand(Cave.SAND_SOURCE):
            old = sand_piece
            sand_piece = self.move_sand(sand_piece)
            if sand_piece is None:
                counter += 1
                self.set_tile(old[0], old[1], Tile.SAND, extend=False)
                sand_piece = Cave.SAND_SOURCE
        return counter


def parse_line(line: str, cave: Cave) -> None:
    prev_coord = None
    for coord in line.split('->'):
        nw_coord = coord.split(',')
        coord = (int(nw_coord[0]), int(nw_coord[1]))

        if prev_coord is not None:
            cave.add_rock_row(prev_coord, coord)

        prev_coord = coord


def parse_input(filename: str) -> Cave:
    ret_cave = Cave()
    with open(filename) as f:
        for line in f.read().splitlines():
            parse_line(line, ret_cave)

    return ret_cave


def main():
    cave = parse_input('input.txt')
    print(cave.count_resting_sand() + 1)



if __name__ == '__main__':
    main()
