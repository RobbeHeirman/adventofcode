import dataclasses


@dataclasses.dataclass
class Box:
    l: int
    w: int
    h: int

    def __repr__(self):
        return f"Box({self.l}X{self.w}X{self.h})"

    def get_side1(self) -> int:
        return self.l * self.w

    def get_side2(self) -> int:
        return self.w * self.h

    def get_side3(self) -> int:
        return self.h * self.l

    def cube(self) -> int:
        return self.w * self.l * self.h

    def get_paper_needed(self) -> int:
        size1 = self.get_side1()
        size2 = self.get_side2()
        size3 = self.get_side3()
        return 2 * (size1 + size2 + size3) + min(size1, size2, size3)

    def get_ribbon_needed(self):
        min1, min2, *_ = sorted([self.l, self.w, self.h])
        return 2 * (min1 + min2) + self.cube()


def read_input(filename: str) -> [Box]:
    with open(filename) as f:
        lines = f.read().splitlines()
    return [Box(*[int(x) for x in line.split("x")]) for line in lines]


def part1(inp: [Box]):
    return sum([box.get_paper_needed() for box in inp])


def part2(inp: [Box]):
    return sum([box.get_ribbon_needed() for box in inp])


def main():
    inp = read_input("input.txt")
    print(f"Answer to part 1: {part1(inp)}")
    print(f"Answer to part 2: {part2(inp)}")


if __name__ == "__main__":
    # print(Box(2, 3, 4).get_ribbon_needed())
    main()
