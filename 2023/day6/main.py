import math
from dataclasses import dataclass
from functools import reduce

from core import Solution


@dataclass
class Race:
    time: int
    distance: int

    def get_error_margin(self):
        # we need to solve hold_time * (total_time - hold_time) >= distance
        # expanding this give total_time * hold_time - hold_time^2 >= distance
        # re_arrange: -hold_time^2 - total_time * hold_time -distance >= 0
        # find 0 points using quadratic equation
        # D = (-time) ** 2 - (4 * -1 * -distance) = time**2 - (4 * distance)
        # x1, x2 = (-total_time +- D) / -2

        d = (self.time ** 2 - 4 * self.distance) ** 0.5
        low_hold, high_hold = tuple(map(lambda sign: (self.time + (sign * d)) / 2, [-1, 1]))

        # We need to round to a millisecond. so low is at least and high utmost press time
        # in the example of max 5 and min 2 we have 4 winnings = 2, 3, 4, 5 => 5 - 2 + 1
        return math.floor(high_hold) - math.ceil(low_hold) + 1


class Day6(Solution):
    @classmethod
    def read_input(cls, lines: [str]) -> [Race]:
        time, distance = map(lambda line: line.split(), lines)
        return list(map(lambda tup: Race(int(tup[0]), int(tup[1])), zip(time[1:], distance[1:])))

    @classmethod
    def solution1(cls, inp: [Race]):
        return reduce(lambda acc, race: acc * race.get_error_margin(), inp, 1)

    @classmethod
    def solution2(cls, inp: [Race]):
        big_time = int("".join(map(lambda race: str(race.time), inp)))
        big_distance = int("".join(map(lambda race: str(race.distance), inp)))
        return Race(big_time, big_distance).get_error_margin()
