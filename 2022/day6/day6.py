import queue


def parse_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def find_marker(data: str, n=4) -> int:
    check_lst = [data[i] for i in range(n)]
    if len(check_lst) == len(set(check_lst)):
        return n

    for i, char in enumerate(data):
        check_lst.append(char)
        if len(check_lst) >= n + 1:
            check_lst.pop(0)
            if len(check_lst) == len(set(check_lst)):
                return i + 1


def ex1() -> int:
    input_str = parse_file('../../../adventofcode/2022/day6.txt')
    return find_marker(input_str)


def ex2() -> int:
    input_str = parse_file('../../../adventofcode/2022/day6.txt')
    return find_marker(input_str, n=14)


def calc_func(x):
    pass


if __name__ == '__main__':

    print(bool(0))
    for i in [-2, -1, 0, 1, 2]:
        print(calc_func(i))
