from typing import List, Reversible, Callable


def count_bits(lines: List[str]) -> List[List[int]]:
    iter_ = lines.__iter__()
    line = iter_.__next__()
    bit_counter = [[int(char == "0"), int(char == "1")] for char in line]
    for line in iter_:
        for i, num in enumerate(line):
            bit_counter[i][int(num)] += 1
    return bit_counter


def create_bit_list(bit_counter: List[List[int]], compare_func) -> List[int]:
    ret = []
    for bit in bit_counter:
        add = compare_func(bit[0], bit[1])
        ret.append(add)
    return ret


def bits_to_decimal(bit_lst: Reversible[str]) -> int:
    return sum([int(bit) * 2 ** i for i, bit in enumerate(reversed(bit_lst))])


def sol_1(lines: List[str]) -> int:
    bit_counter = count_bits(lines)

    alpha = 0
    gamma = 0
    for i, win in enumerate(reversed(bit_counter)):
        is_one = win[1] > win[0]
        alpha += int(is_one) * 2 ** i
        gamma += int(not is_one) * 2 ** i
    return alpha * gamma


def find_bit_string(lines: List[str], oxygen_generator=True) -> str:
    compare_func: Callable
    if oxygen_generator:
        compare_func = lambda zero, one: 1 if one >= zero else 0
    else:
        compare_func = lambda zero, one: 0 if zero <= one else 1

    reduce_lst = lines[:]
    for i in range(len(lines[0])):
        bit_counter = count_bits(reduce_lst)
        bit_lst = create_bit_list(bit_counter, compare_func)
        new_reduce_lst = []
        for bit_line in reduce_lst:
            if int(bit_line[i]) == bit_lst[i]:
                new_reduce_lst.append(bit_line)
        reduce_lst = new_reduce_lst
        if len(reduce_lst) == 1:
            return reduce_lst[0]

    return reduce_lst[0]


def sol_2(lines: List[str]) -> int:
    oxygen = find_bit_string(lines)
    co2 = find_bit_string(lines, False)

    oxygen_decimal = bits_to_decimal(oxygen)
    co2_decimal = bits_to_decimal(co2)

    return oxygen_decimal * co2_decimal


if __name__ == "__main__":
    with open("../../../adventofcode/2021/day3.txt") as file:
        input_ = file.read().splitlines()
    # print(sol_1(input_))
    print(sol_2(input_))
