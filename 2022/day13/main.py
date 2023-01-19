import dataclasses
import enum
from functools import cmp_to_key
from typing import Union, List

Packet = Union[int, List['ListComponent']]


class Decide(enum.Enum):
    TRUE = 0
    FALSE = 1
    EQUAL = 2


@dataclasses.dataclass
class PacketPair:
    packet1: Packet
    packet2: Packet

    def compare(self):
        compare = self._compare_lists(self.packet1, self.packet2)
        if compare in [Decide.TRUE, Decide.EQUAL]:
            return True
        return False

    @staticmethod
    def compare_final(el1, el2):
        decide = PacketPair.compare_packets(el1, el2)
        if decide in [Decide.TRUE, Decide.EQUAL]:
            return -1
        return 1

    @staticmethod
    def compare_packets(el1, el2) -> Decide:

        if isinstance(el1, list):
            if isinstance(el2, list):
                return PacketPair._compare_lists(el1, el2)
            else:
                return PacketPair._compare_list_int(el1, el2)
        else:
            if isinstance(el2, int):
                return PacketPair._compare_ints(el1, el2)
            else:
                return PacketPair._compare_list_int(el1, el2)

    @staticmethod
    def _compare_lists(list1, list2) -> Decide:
        for i in range(len(list1)):
            if i == len(list2):
                return Decide.FALSE
            decide = PacketPair.compare_packets(list1[i], list2[i])
            if decide == Decide.TRUE:
                return Decide.TRUE
            elif decide == Decide.FALSE:
                return Decide.FALSE

        if len(list1) < len(list2):
            return Decide.TRUE

        return Decide.EQUAL

    @staticmethod
    def _compare_ints(el1: int, el2: int) -> Decide:
        if el1 < el2:
            return Decide.TRUE
        elif el1 > el2:
            return Decide.FALSE

        return Decide.EQUAL

    @staticmethod
    def _compare_list_int(el1, el2) -> Decide:
        if isinstance(el1, int):
            el1 = [el1]
        if isinstance(el2, int):
            el2 = [el2]
        return PacketPair._compare_lists(el1, el2)


def parse_input(filename: str) -> List[PacketPair]:
    with open(filename) as f:
        return [parse_packet_pair(pair_str) for pair_str in f.read().split('\n\n')]


def parse_packet_pair(pair_input: str) -> PacketPair:
    return PacketPair(*[parse_packet(pack_str) for pack_str in pair_input.splitlines()])


def parse_packet(packet_input: str) -> Packet:
    list_stack = []
    char_parsed = []
    for char in packet_input:
        if char == '[':
            nw_list = []
            if list_stack:
                list_stack[-1].append(nw_list)
            list_stack.append(nw_list)
        # if we close a list
        elif char == ']':
            # if last list is closed we return last list = root list
            if char_parsed:
                list_stack[-1].append(int("".join(char_parsed)))
                char_parsed = ''
            if len(list_stack) == 1:
                return list_stack[0]
            else:
                list_stack.pop()
        elif char == ',':
            if char_parsed:
                list_stack[-1].append(int("".join(char_parsed)))
            char_parsed = []
        elif char == ' ':
            continue
        else:
            char_parsed.append(char)


def main():
    packet_pairs = parse_input('input.txt')
    indices_list = []
    # for i, packet_pair in enumerate(packet_pairs):
    #     if packet_pair.compare():
    #         indices_list.append(i + 1)

    packets = []
    for pair in packet_pairs:
        packets.append(pair.packet1)
        packets.append(pair.packet2)

    divider1 = [[2]]
    divider2 = [[6]]
    packets.append(divider1)
    packets.append(divider2)
    packets.sort(key=cmp_to_key(PacketPair.compare_final))
    ind1 = packets.index(divider1) + 1
    ind2 = packets.index(divider2) + 1
    print(ind1 * ind2)

if __name__ == '__main__':
    main()
