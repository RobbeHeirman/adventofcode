import functools
from collections import namedtuple
from dataclasses import dataclass
from typing import ClassVar, TypeVar, Type, Iterable

from core.solution import Solution

card_count = namedtuple("card_count", "card count")


def create_ordered_chars(start: str, length):
    start_num = ord(start)
    return list(map(lambda i: chr(start_num + i), range(length)))


CARD_ORDER = ["A", "K", "Q", "J", "T"] + list(reversed(create_ordered_chars("2", 8)))
CARD_ORDER = dict(map(lambda entry: (entry[1], len(CARD_ORDER) - entry[0]), enumerate(CARD_ORDER)))


@dataclass
class Hand:
    CARD_ORDER: ClassVar[{str: int}] = CARD_ORDER

    cards: str
    cards_counted: list[card_count]
    bid: int

    def get_first_ordering(self):
        most_same_card = self.cards_counted[0]
        if most_same_card.count >= 5:
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

    @classmethod
    def map_cards_to_order(cls, inp: str) -> Iterable[int]:
        return map(lambda s: cls.CARD_ORDER[s], inp)

    def __lt__(self, other: "Hand"):
        my_first_ordering = self.get_first_ordering()
        there_first_ordering = other.get_first_ordering()
        if my_first_ordering != there_first_ordering:
            return my_first_ordering < there_first_ordering

        my_ordered_cards = self.map_cards_to_order(self.cards)
        there_ordered_cards = self.map_cards_to_order(other.cards)
        card_diff = map(lambda entry: entry[0] - entry[1], zip(my_ordered_cards, there_ordered_cards))
        card_diff = next(filter(lambda x: x != 0, card_diff))
        return card_diff < 0


JOKER_CARD_ORDER = ["A", "K", "Q", "T"] + list(reversed(create_ordered_chars("2", 8))) + ["J"]
JOKER_CARD_ORDER = dict(map(lambda entry: (entry[1], len(JOKER_CARD_ORDER) - entry[0]), enumerate(JOKER_CARD_ORDER)))


@dataclass
class JokerHand(Hand):
    CARD_ORDER: ClassVar[{str: int}] = JOKER_CARD_ORDER

    def __post_init__(self):
        try:
            joker_card = next(filter(lambda c: c.card == "J", self.cards_counted))
            j_count = joker_card.count

            remainder = list(filter(lambda c: c.card != "J", self.cards_counted))
            if not remainder:
                return
            remainder[0] = card_count(remainder[0].card, remainder[0].count + j_count)
            self.cards_counted = remainder

        except StopIteration:
            pass


def convert_to_sorted_count_tuples(inp: str):
    unique_chars = set(inp)
    tuples = map(lambda c: card_count(c, inp.count(c)), unique_chars)
    tuples = sorted(tuples, key=lambda c_count: -CARD_ORDER[c_count.card])
    return list(sorted(tuples, key=lambda c_count: -c_count.count))


T = TypeVar("T", bound=Hand)


def create_hand(inp: str, init_cls: Type[T] = Hand) -> T:
    cards_str, bid = inp.split()
    cards = convert_to_sorted_count_tuples(cards_str)
    return init_cls(cards_str, cards, int(bid))


class Day7(Solution):

    @classmethod
    def read_input(cls, lines: [str]) -> [str]:
        return lines

    @classmethod
    def solution1(cls, inp: [str]):
        inp = list(sorted(map(create_hand, inp)))
        return functools.reduce(lambda acc, c: acc + ((c[0] + 1) * c[1].bid), enumerate(inp), 0)

    @classmethod
    def solution2(cls, inp: T):
        inp = list(sorted(map(lambda c: create_hand(c, JokerHand), inp)))
        return functools.reduce(lambda acc, c: acc + ((c[0] + 1) * c[1].bid), enumerate(inp), 0)
