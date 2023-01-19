import abc
import dataclasses


@dataclasses.dataclass
class Coordinate:
    x: int
    y: int


class GridTile(abc.ABC):

    def __init__(self, cave, coordinate, repr_):
        self._cave = cave
        self.coordinate = coordinate
        self._repr = repr_

    def update(self):
        pass

    @staticmethod
    def is_solid():
        return True

    def __str__(self):
        return self._repr

    def __repr__(self):
        return self._repr


class Air(GridTile):

    def __init__(self, cave, coordinate):
        super().__init__(cave, coordinate, '.')

    @staticmethod
    def is_solid():
        return False


class Stone(GridTile):
    def __init__(self, cave, coordinate):
        super().__init__(cave, coordinate, '#')


class Sand(GridTile):
    def __init__(self, cave, coordinate):
        super().__init__(cave, coordinate, 'O')


class SandSource(GridTile):
    def __init__(self, cave, coordinate):
        super().__init__(cave, coordinate, '+')


class Cave:

    def __init__(self):
        self.grid = []
        self.cave_width = 0
        self.cave_height = 0

        self.extend_cave_width(501)
        self.extend_height(1)
        self._sand_source = SandSource(self, Coordinate(0, 500))
        self.grid[0][500] = self._sand_source

    def __str__(self):
        ret = ''
        for row in self.grid:
            for cell in row:
                ret += f'{cell}'
            ret += '\n'
        return ret

    def extend_cave_width(self, x: int):
        if x <= self.cave_width:
            return

        extend_width = self.cave_width - x
        for i, row in enumerate(self.grid):
            for extend_num in range(extend_width):
                j = self.cave_width + extend_num
                row.append(Air(self, Coordinate(i, j)))

        self.cave_width = x

    def extend_height(self, y: int):
        if y <= self.cave_height:
            return

        extend_height = y - self.cave_height
        for i_extend in range(extend_height):
            i = self.cave_height + i_extend
            self.grid.append([Air(self, Coordinate(i, j)) for j in range(self.cave_width)])
        self.cave_height = y

    def set_tile(self, tile: GridTile):
        self.extend_cave_width(tile.coordinate.x + 1)
        self.extend_height(tile.coordinate.y + 1)
        print(tile.coordinate.y, ' ', sel)
        self.grid[tile.coordinate.y][tile.coordinate.x] = tile

    def add_rock_line(self, coord1: Coordinate, coord2: Coordinate):

        x_small, x_big = tuple(sorted((coord1.x, coord2.x)))
        y_small, y_big = tuple(sorted((coord1.y, coord2.y)))

        for x in range(x_small, x_big):
            stone = Stone(self, Coordinate(x, y_small))
            self.set_tile(stone)

        for y in range(y_small, y_big):
            stone = Stone(self, Coordinate(x_small, y))
            self.set_tile(stone)


def parse_input(filename: str) -> Cave:
    cave = Cave()
    with open(filename) as f:
        for line in f.read().splitlines():
            parse_line(line, cave)


def parse_line(line: str, cave: Cave):
    coordinates = line.split('->')
    prev_coord = None
    for cord_str in coordinates:
        x1, y1 = cord_str.split(',')
        coord1 = Coordinate(int(x1), int(y1))

        if prev_coord:
            cave.add_rock_line(prev_coord, coord1)
        prev_coord = coord1



def main():
    parse_input('input2.txt')


if __name__ == '__main__':
    main()
