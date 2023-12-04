import itertools
from dataclasses import dataclass
from core.solution import Solution


@dataclass(frozen=True)
class Card:
    id: int
    winning_numbers_count: int

    def get_winning_numbers(self) -> int:
        return self.winning_numbers_count

    def get_points_worth(self):
        return 0 if self.winning_numbers_count == 0 else 2 ** (self.winning_numbers_count - 1)


def convert_str_ints(inp: str) -> set[int]:
    return set(map(int, inp.split()))


def string_to_card(string: str) -> Card:
    id_part, rest = string.split(":")
    identifier = int(id_part.split()[1])
    winning, my = rest.split("|")
    win_count = convert_str_ints(winning).intersection(convert_str_ints(my))
    return Card(identifier, len(win_count))


def create_copies(card: Card, other_cards: [Card]) -> [Card]:
    max_index = min(card.id + card.winning_numbers_count, len(other_cards))
    return map(lambda i: other_cards[i], range(card.id, max_index))


def copy_recursive(cards: [Card], original=None) -> [Card]:
    if original is None:
        original = cards

    copies = map(lambda card: create_copies(card, original), cards)
    chained = itertools.chain(*copies)
    if elements := list(chained):
        return copy_recursive(elements, original) + cards
    return cards


class Day4(Solution):
    @classmethod
    def read_input(cls, lines: [str]) -> [Card]:
        return list(map(string_to_card, lines))

    @classmethod
    def solution1(cls, inp: [Card]) -> int:
        return sum(map(lambda card: card.get_points_worth(), inp))

    @classmethod
    def solution2(cls, inp: [Card]) -> int:
        return len(copy_recursive(inp))
