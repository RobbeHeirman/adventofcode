def find_shared_article(input_: str) -> str:
    rucksack1 = input_[:len(input_) // 2]
    rucksack2 = input_[len(input_) // 2:]

    rucksack1 = set(rucksack1)
    rucksack2 = set(rucksack2)

    intersect = rucksack1.intersection(rucksack2)
    return intersect.pop()


def find_badge(rucksack1: str, rucksack2: str, rucksack3: str) -> str:
    set1 = set(rucksack1)
    set2 = set(rucksack2)
    set3 = set(rucksack3)

    inters1 = set1.intersection(set2)
    inters2 = inters1.intersection(set3)
    return inters2.pop()


def find_prio_value(char: str) -> int:
    if char.islower():
        return ord(char) - ord("a") + 1
    return ord(char) - ord("A") + 27


def day1_1() -> int:
    with open("input.txt") as f:
        return sum([find_prio_value(find_shared_article(line)) for line in f])


def day1_2() -> int:
    with open('input.txt') as f:
        group_lst = []
        sum_ = 0
        for line in f.readlines():
            group_lst.append(line[:-1])
            if len(group_lst) == 3:
                badge = find_badge(*group_lst)
                sum_ += find_prio_value(badge)
                group_lst = []

        return sum_


if __name__ == '__main__':
    print(day1_2())
