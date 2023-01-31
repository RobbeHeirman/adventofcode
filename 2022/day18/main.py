import dataclasses
import enum
import functools
import itertools


class CubeType(enum.Enum):
    LAVA = enum.auto()
    AIR = enum.auto()


@dataclasses.dataclass(unsafe_hash=False)
class Cube:
    x: int
    y: int
    z: int
    neighbors: set = dataclasses.field(default_factory=set)
    type: CubeType = CubeType.LAVA
    is_trapped: bool = False

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def combined_coordinates(self):
        return self.x + self.y + self.z

    def coordinates_as_tuple(self) -> tuple[int, int, int]:
        return self.x, self.y, self.z

    def is_neighbor(self, cube: "Cube") -> bool:
        counter = functools.reduce(lambda a, b: a + 1 if b[0] == b[1] else a,
                                   zip(self.coordinates_as_tuple(), cube.coordinates_as_tuple()),
                                   0
                                   )
        if abs(self.combined_coordinates() - cube.combined_coordinates()) != 1 and counter != 1:
            return False
        return True


class Grid:
    def __init__(self):
        self._x_dict = {}
        self._y_dict = {}
        self._z_dict = {}

    def add_cube(self, cube: Cube):
        self._x_dict.setdefault(cube.x, set()).add(cube)
        self._y_dict.setdefault(cube.y, set()).add(cube)
        self._z_dict.setdefault(cube.z, set()).add(cube)

    def add_cubes(self, cubes: list[Cube]) -> None:
        for cube in cubes:
            self.add_cube(cube)

    def get_cube_at_location(self, x, y, z):
        if remainder := self._x_dict.setdefault(x, set()) \
                .intersection(self._y_dict.setdefault(y, set())) \
                .intersection(self._z_dict.setdefault(z, set())):
            return next(iter(remainder))
        raise ValueError

    def get_neighbors(self, cube: Cube) -> list[Cube]:
        sets = [
            self._x_dict.setdefault(cube.x, set()),
            self._y_dict.setdefault(cube.y, set()),
            self._z_dict.setdefault(cube.z, set())
        ]
        ret = []
        for dicts in itertools.combinations(sets, 2):
            set1, set2 = dicts
            candidate_neighbors = set1.intersection(set2)

            ret.extend(
                list(filter(lambda neighbor: cube.is_neighbor(neighbor) and neighbor is not cube, candidate_neighbors)))
        return ret


def parse_input(filename: str) -> list[Cube]:
    with open(filename) as f:
        return [Cube(*[int(i) for i in line.split(',')]) for line in f.read().splitlines()]


def main():
    cubes = parse_input("input.txt")
    grid = Grid()
    grid.add_cubes(cubes)
    for cube in cubes:
        neighbors = grid.get_neighbors(cube)
        cube.neighbors = neighbors


    return functools.reduce(lambda sum_, element: sum_ + 6 - len(element.neighbors), cubes, 0)

    # def recursive_is_trapped_check(cube: Cube, checked_cubes) -> bool:
    #     if cube.type == CubeType.LAVA:
    #         cube.is_trapped = True
    #         return True
    #
    #     dimensions = [cube.x, cube.y, cube.z]
    #     if min(dimensions) == 0 or dimensions[0] == max_x or dimensions[1] == max_y or dimensions[2] == max_z:
    #         cube.is_trapped = False
    #         return False
    #
    #     trap_check = []
    #     for i in range(len(dimensions)):
    #         for direction in [-1, 1]:
    #             dimensions[i] += direction
    #             nx, ny, nz = dimensions
    #
    #             location = x_dict.setdefault(nx, set()) \
    #                 .intersection(y_dict.setdefault(ny, set())) \
    #                 .intersection(z_dict.setdefault(nz, set()))
    #             if location:
    #                 location = location.pop()
    #             else:
    #                 location = Cube(nx, ny, nz, type=CubeType.AIR)
    #                 air_cubes.add(location)
    #
    #             if location not in checked_cubes:
    #                 checked_cubes.add(location)
    #                 recursive_is_trapped_check(location, checked_cubes)
    #
    #             trap_check.append(location.is_trapped)
    #
    #     cube.is_trapped = bool(min(trap_check))
    #     return cube.is_trapped
    #
    # for cube in cubes:
    #     checked_cubes = set()
    #     dimensions = [cube.x, cube.y, cube.z]
    #     for i in range(len(dimensions)):
    #         for direction in [-1, 1]:
    #             dimensions[i] += direction
    #             nx, ny, nz = dimensions
    #             location = x_dict.setdefault(nx, set()) \
    #                 .intersection(y_dict.setdefault(ny, set())) \
    #                 .intersection(z_dict.setdefault(nz, set()))
    #
    #             location = location.pop() if location else Cube(nx, ny, nz, type=CubeType.AIR)
    #             recursive_is_trapped_check(location, checked_cubes)
    #
    # return sum(cube.uncovered for cube in cubes)


if __name__ == "__main__":
    print(main())
    # tp = (28, 44)
    # tp2 = (44, 28)
    # print(hash(tp) == hash(tp2))
