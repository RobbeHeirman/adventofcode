def read_input(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def calculate_floor(inp: str, start_floor: int, stop_floor=None) -> int:
    for pos, ch in enumerate(inp):
        if ch == "(":
            start_floor += 1
        if ch == ")":
            start_floor -= 1
        if start_floor is not None and stop_floor == start_floor:
            return pos + 1
    return start_floor


def part1(inp: str) -> int:
    return calculate_floor(inp, 0)


def part2(inp: str) -> int:
    return calculate_floor(inp, 0, -1)


def main():
    inp = read_input("input.txt")
    print(f"answer to part 1 is {part1(inp)}")
    print(f"answer to part 2 is {part2(inp)}")


if __name__ == "__main__":
    main()
