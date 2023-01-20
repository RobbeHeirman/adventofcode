import dataclasses
import itertools


@dataclasses.dataclass(unsafe_hash=False)
class Cube:
    x: int
    y: int
    z: int
    uncovered: int = 6

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def combined_coordinates(self):
        return self.x + self.y + self.z


def parse_input(filename: str) -> list[Cube]:
    with open(filename) as f:
        return [Cube(*[int(i) for i in line.split(',')]) for line in f.read().splitlines()]


def main():
    cubes = parse_input("input.txt")
    x_dict = {}
    y_dict = {}
    z_dict = {}
    for cube in cubes:
        x_neighbors = x_dict.setdefault(cube.x, set())
        y_neighbors = y_dict.setdefault(cube.y, set())
        z_neighbors = z_dict.setdefault(cube.z, set())
        sets = [x_neighbors, y_neighbors, z_neighbors]
        for comb in itertools.combinations(sets, 2):
            set1, set2 = comb
            candidate_neighbors = set1.intersection(set2)
            for candidate_neighbor in candidate_neighbors:
                if abs(candidate_neighbor.combined_coordinates() - cube.combined_coordinates()) == 1:
                    candidate_neighbor.uncovered -= 1
                    cube.uncovered -= 1

        for set_ in sets:
            set_.add(cube)

    return sum(cube.uncovered for cube in cubes)


if __name__ == "__main__":
    print(main())
