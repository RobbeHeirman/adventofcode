def read_input(filename: str) -> str:
    with open(filename) as f:
        return f.read()


MOVE_DICT = {
    ">": (1, 0),
    "^": (0, 1),
    "<": (-1, 0),
    "v": (0, -1)
}


def santa_moves(start_pos: (int, int), move: str) -> (int, int):
    return tuple(t1 + t2 for t1, t2 in zip(start_pos, MOVE_DICT[move]))


def visit_houses(inp: str, santas=1) -> int:
    pos = [(0, 0) for _ in range(santas)]
    result = {pos[0]}
    for i in range(0, len(inp), santas):
        moves = inp[i: i + santas]
        pos = [santa_moves(pos, move) for pos, move in zip(pos, moves)]
        result.update(pos)
    return len(result)


def main():
    inp = read_input("input.txt")
    print(f"result of part1: {visit_houses(inp, 1)}")
    print(f"result of part2: {visit_houses(inp, 2)}")


if __name__ == "__main__":
    main()
