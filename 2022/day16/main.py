import dataclasses
import re


@dataclasses.dataclass
class Neighbor:
    valve: 'Valve'
    length: int = 1


@dataclasses.dataclass
class Valve:
    id: str
    pressure: int = 0
    neighbors: list = dataclasses.field(default_factory=list)

    def add_neighbor(self, neighbor: 'Valve') -> None:
        self.neighbors.append(neighbor)

    def neighbor_reduction(self):
        """
        The goal is to
        """


def parse_input(filename: str) -> dict[Valve]:
    pressure_regex = re.compile('\d+')
    id_regex = re.compile('[A-Z]{2}')

    existing_valves = {}
    with open(filename) as f:
        for line in f.read().splitlines():
            root_id, *neighbors = id_regex.findall(line)
            pressure = int(pressure_regex.findall(line)[0])

            root_valve = existing_valves.setdefault(root_id, Valve(id=root_id, pressure=pressure))
            root_valve.pressure = pressure

            for neighbor_id in neighbors:
                neighbor = existing_valves.setdefault(neighbor_id, Valve(id=neighbor_id))
                root_valve.add_neighbor(neighbor)

        return existing_valves


def main():
    valves = parse_input('input.txt')


if __name__ == '__main__':
    main()
