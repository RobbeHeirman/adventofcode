import functools
from collections import namedtuple
from dataclasses import dataclass
from typing import ClassVar

from core.solution import Solution, T

card_count = namedtuple("card_count", "card count")


def create_ordered_chars(start: str, length):
    start_num = ord(start)
    return list(map(lambda i: chr(start_num + i), range(length)))


CARD_ORDER = ["A", "K", "Q", "J", "T"] + list(reversed(create_ordered_chars("2", 8)))
CARD_ORDER = dict(map(lambda entry: (entry[1], len(CARD_ORDER) - entry[0]), enumerate(CARD_ORDER)))


@dataclass(frozen=True)
class Hand:
    CARD_ORDER: ClassVar[{str: int}] = CARD_ORDER

    cards: str
    cards_counted: list[card_count]
    bid: int

    def get_first_ordering(self):
        most_same_card = self.cards_counted[0]
        if most_same_card.count == 5:
            return 6
        elif most_same_card.count == 4:
            return 5
        elif most_same_card.count == 3:
            second_most_card = self.cards_counted[1]
            return 4 if second_most_card.count == 2 else 3
        elif most_same_card.count == 2:
            second_most_card = self.cards_counted[1]
            return 2 if second_most_card.count == 2 else 1
        return 0

    def secondary_ordering(self):
        return int("".join(map(lambda c: str(self.__class__.CARD_ORDER[c]), self.cards)))

    def __lt__(self, other: "Hand"):
        my_first_ordering = self.get_first_ordering()
        there_first_ordering = other.get_first_ordering()
        if my_first_ordering != there_first_ordering:
            return my_first_ordering < there_first_ordering

        for my_c, there_c in zip(self.cards, other.cards):
            if my_c != there_c:
                return CARD_ORDER[my_c] < CARD_ORDER[there_c]


JOKER_CARD_ORDER = ["A", "K", "Q", "T"] + list(reversed(create_ordered_chars("2", 8))) + ["J"]
JOKER_CARD_ORDER = dict(map(lambda entry: (entry[1], len(CARD_ORDER) - entry[0]), enumerate(CARD_ORDER)))


class JokerHand(Hand):

    def get_first_ordering(self):
        jokers = self.cards.count("J")


def convert_to_sorted_count_tuples(inp: str):
    unique_chars = set(inp)
    tuples = map(lambda c: card_count(c, inp.count(c)), unique_chars)
    tuples = sorted(tuples, key=lambda c_count: -CARD_ORDER[c_count.card])
    return list(sorted(tuples, key=lambda c_count: -c_count.count))


def create_hand(inp: str) -> Hand:
    cards_str, bid = inp.split()
    cards = convert_to_sorted_count_tuples(cards_str)
    return Hand(cards_str, cards, int(bid))


class Day7(Solution):

    @classmethod
    def read_input(cls, lines: [str]) -> T:
        return list(map(create_hand, lines))

    @classmethod
    def solution1(cls, inp: T):
        inp = list(sorted(inp))
        return functools.reduce(lambda acc, c: acc + ((c[0] + 1) * c[1].bid), enumerate(inp), 0)

    @classmethod
    def solution2(cls, inp: T):
        pass
