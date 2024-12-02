from dataclasses import dataclass
from functools import reduce

import core as solution

MAX_VALS = {
    "red": 12,
    "green": 13,
    "blue": 14
}


@dataclass
class Set:
    drawn_cubes: {str: int}

    def is_set_possible(self) -> bool:
        return min(map(lambda entry: MAX_VALS[entry[0]] >= entry[1], self.drawn_cubes.items()))


@dataclass
class Game:
    id: int
    sets: [Set]

    def is_game_possible(self) -> bool:
        return min(map(lambda st: st.is_set_possible(), self.sets))

    def _find_max_for_key(self, key) -> int:
        return max(map(lambda st: st.drawn_cubes.get(key, 0), self.sets))

    def find_power_min_cubes_needed(self) -> int:
        max_needed = map(lambda key: self._find_max_for_key(key), MAX_VALS.keys())
        return reduce(lambda x, y: x * y, max_needed)


def _color_string_splitter(color_str: str) -> (str, int):
    amount, color = color_str.split()
    return color, int(amount)


def _make_color_dict(color_strs: list[str]) -> {str: int}:
    return dict(map(_color_string_splitter, color_strs))


def create_set(set_string: str) -> Set:
    color_strs = set_string.split(",")
    return Set(_make_color_dict(color_strs))


def create_game(game_str: str) -> Game:
    identifier_str, remainder = game_str.split(":")
    game_identifier = int(identifier_str.split()[1])

    set_strings = remainder.split(";")
    sets = list(map(create_set, set_strings))

    return Game(game_identifier, sets)


class Day2(solution.Solution):
    @classmethod
    def read_input(cls, lines: [str]) -> [Game]:
        return list(map(create_game, lines))

    @classmethod
    def solution1(cls, inp: [Game]) -> int:
        possible_games = filter(lambda game: game.is_game_possible(), inp)
        return reduce(lambda acc, game: acc + game.id, possible_games, 0)

    @classmethod
    def solution2(cls, inp: [Game]) -> int:
        return sum(map(lambda game: game.find_power_min_cubes_needed(), inp))
