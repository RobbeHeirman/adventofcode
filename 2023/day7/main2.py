import itertools
from typing import List, Tuple

# Day 7: Camel Cards

test_data = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''.split('\n')

card_types = {'FIVE': '6', 'FOUR': '5', 'FULL_HOUSE': '4', 'THREE': '3', 'TWO_PAIRS': '2', 'PAIR': '1', 'HIGH': '0'}


def parse_input(data) -> List[Tuple[str, int]]:
    hands = []
    for line in data:
        hand_str, bid = line.split()
        hands.append((hand_str, int(bid)))
    return hands


def count_n_tuple(hand_str, n):
    """Count how many n-tuples (pairs, triplets, etc.) are in a hand"""
    unique_cards = set(hand_str)
    return sum([1 for card in unique_cards if hand_str.count(card) == n])


def hexify(hand_str, has_joker=False):
    """Replace cards (King, Queen etc.) to upper hex values"""
    if has_joker:
        hand_str = hand_str.replace('J', '1')
    return hand_str.replace('A', 'E').replace('K', 'D').replace('Q', 'C').replace('J', 'B').replace('T', 'A')


def get_value(hand_str: str, orig_hand=None) -> int:
    if count_n_tuple(hand_str, 5) == 1:
        prefix = card_types['FIVE']
    elif count_n_tuple(hand_str, 4) == 1:
        prefix = card_types['FOUR']
    elif count_n_tuple(hand_str, 3) == 1:
        if count_n_tuple(hand_str, 2) == 1:
            prefix = card_types['FULL_HOUSE']
        else:
            prefix = card_types['THREE']
    elif count_n_tuple(hand_str, 2) == 2:
        prefix = card_types['TWO_PAIRS']
    elif count_n_tuple(hand_str, 2) == 1:
        prefix = card_types['PAIR']
    else:
        prefix = card_types['HIGH']

    if orig_hand is not None:
        hex_hand = hexify(orig_hand, True)
    else:
        hex_hand = hexify(hand_str)
    value = prefix + hex_hand
    return int(value, 16)


def part1(data: List[str]):
    hands: List[Tuple[str, int, int]] = []
    for hand, bid in parse_input(data):
        hands.append((hand, bid, get_value(hand)))
    hands = sorted(hands, key=lambda c: c[2])
    return sum([hand[1] * (i + 1) for (i, hand) in enumerate(hands)])


def get_hand_candidates(hand, cards) -> List[str]:
    new_hands = []
    new_hand = hand.replace('J', '')
    for replacement in itertools.combinations_with_replacement(cards, hand.count('J')):
        new_hands.append(new_hand + ''.join(replacement))
    return new_hands


def part2(data: List[str]):
    hands = []
    for hand, bid in parse_input(data):
        hand_candidates = [hand]
        if 'J' in hand:
            card_candidates = set(hand.replace('J', ''))
            if len(card_candidates) == 0:
                card_candidates = {'A'}
            hand_candidates = get_hand_candidates(hand, card_candidates)

        possible_values = [get_value(hand_candidate, hand) for hand_candidate in hand_candidates]
        best_value = sorted(possible_values)[-1]
        hands.append((hand, bid, best_value))
    hands = sorted(hands, key=lambda c: c[2])
    return sum([hand[1] * (i + 1) for (i, hand) in enumerate(hands)])


def main():
    with open('input.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    part1_result = part1(data)


    part2_test_result = part2(test_data)

    part2_result = part2(data)
    assert part2_result == 251421071, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()