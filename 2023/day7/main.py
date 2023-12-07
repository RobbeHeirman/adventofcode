from collections import namedtuple
from dataclasses import dataclass

from core.solution import Solution, T

card_count = namedtuple("card_count", "card count")


def create_ordered_chars(start: str, length):
    start_num = ord(start)
    return list(map(lambda i: chr(start_num + i), range(length)))


CARD_ORDER = ["A", "K", "Q", "J", "T"] + list(reversed(create_ordered_chars("2", 8)))


@dataclass(frozen=True)
class Hand:
    cards_counted: list[card_count]
    bid: int

    def get_hand_score(self):
        most_same_card = self.cards_counted[0]



def convert_to_sorted_count_tuples(inp: str):
    unique_chars = set(inp)
    tuples = map(lambda c: card_count(c, inp.count(c)), unique_chars)
    return list(sorted(tuples, key=lambda c_count: -c_count.count))


def create_hand(inp: str) -> Hand:
    cards_str, bid = inp.split()
    cards = convert_to_sorted_count_tuples(cards_str)
    return Hand(cards, cards_str)


class Day7(Solution):
    @classmethod
    def read_input(cls, lines: [str]) -> T:
        return list(map(create_hand, lines))

    @classmethod
    def solution1(cls, inp: T):
        pass

    @classmethod
    def solution2(cls, inp: T):
        pass
