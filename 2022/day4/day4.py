from typing import Union


class Range:
    def __init__(self, start, end):
        self.start = int(start)
        self.end = int(end)

    def __contains__(self, item: Union[int, "Range"]):
        if isinstance(item, int):
            return self.start <= item <= self.end
        return item.start >= self.start and item.end <= self.end

    def overlap(self, item: "Range"):
        return (item.start in self or item.end in self) or (self.start in item or self.end in item)

def str_to_range_pair(string: str) -> [Range, Range]:
    pairs = string.split(",")
    return [Range(*pair.split('-')) for pair in pairs]


def main():
    with open("../../../adventofcode/2022/day4.txt") as f:
        counter = 0
        counter2 = 0
        for line in f:
            pairs = str_to_range_pair(line[:-1])
            counter += pairs[0] in pairs[1] or pairs[1] in pairs[0]
            counter2 += pairs[0].overlap(pairs[1])
        print(counter)
        print(counter2)
if __name__ == "__main__":
    main()