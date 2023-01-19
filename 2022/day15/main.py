import dataclasses
from typing import List, Tuple

CONCIDER_ROW = 2000000

# ONCIDER_ROW = 10


def manhatten_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


@dataclasses.dataclass
class BeaconSensor:
    sensor: (int, int)
    beacon: (int, int)

    def invalid_positions(self) -> List[Tuple[int, int]]:
        invalid_pos = []

        if not self.sensor[1] - self.manhatten_distance <= CONCIDER_ROW <= self.sensor[1] + self.manhatten_distance:
            return invalid_pos

        distance_to_row = abs(self.sensor[1] - CONCIDER_ROW)
        amount_of_pos = self.manhatten_distance - distance_to_row
        for x in range(self.sensor[0] - amount_of_pos, self.sensor[0] + amount_of_pos):
            invalid_pos.append((x, CONCIDER_ROW))

        # for x in range(self.sensor[0] - self.manhatten_distance, self.sensor[0] + self.manhatten_distance + 1):
        #     x_distance = abs(self.sensor[0] - x)
        #     x_diff = self.manhatten_distance - x_distance
        #     for y in range(self.sensor[1] - x_diff, self.sensor[1] + x_diff + 1):
        #         print((x, y))
        #         if y == 2000000:
        #             invalid_pos.append((x, y))

        return invalid_pos

        
    @property
    def manhatten_distance(self):
        return manhatten_distance(self.sensor[0], self.sensor[1], self.beacon[0], self.beacon[1])


def parse_line(line: str):
    line = line.split()

    sensor = (line[2], line[3])
    sensor = (int(sensor[0][2:-1]), int(sensor[1][2:-1]))

    beacon = (line[-2], line[-1])
    beacon = (int(beacon[0][2:-1]), int(beacon[1][2:]))
    return BeaconSensor(sensor=sensor, beacon=beacon)


def parse_input(filename: str) -> List[BeaconSensor]:
    ret = []
    with open(filename) as f:
        for line in f.read().splitlines():
            ret.append(parse_line(line))
    return ret


def draw_map(inp, sensors_beacons):
    sensors = [pair.sensor for pair in sensors_beacons]
    beacons = [pair.beacon for pair in sensors_beacons]

    x_vals = list(map(lambda tup: tup[0], inp)) + [sensor[0] for sensor in sensors] + [beacon[0] for beacon in beacons]
    x_vals.sort()
    x_min = x_vals[0]
    x_max = x_vals[-1]

    y_vals = list(map(lambda tup: tup[1], inp)) + [sensor[1] for sensor in sensors] + [beacon[1] for beacon in beacons]
    y_vals.sort()
    y_min = y_vals[0]
    y_max = y_vals[-1]

    spacing = 3
    ret = ' ' * spacing
    ret += ''.join([f'{i:{spacing}}' for i in range(x_min, x_max + 1)])
    ret += '\n'
    for y in range(y_min, y_max + 1):
        ret += f'{y:>{spacing}}: '
        for x in range(x_min, x_max + 1):

            if (x, y) in sensors:
                symbol = 'S'
            elif (x, y) in beacons:
                symbol = 'B'
            elif (x, y) in inp:
                symbol = '#'
            else:
                symbol = '.'
            ret += f"{symbol:{spacing}}"
        ret += '\n'

    return ret


def main():
    inp = parse_input('input.txt')
    not_possible = set()
    for i, pair in enumerate(inp):
        not_possible.update(pair.invalid_positions())

    not_possible = not_possible.difference(set([pair.sensor for pair in inp]))
    print(len(not_possible))



if __name__ == '__main__':
    main()
