def file_to_set(file):
    with open(file) as f:
        return set(int(val.strip()) for val in f.readlines())


def day_1(total: int) -> int:
    input_set = file_to_set('input_day1.txt')
    result = input_set & set(total - val for val in input_set)
    return result.pop() * result.pop()


def day_1_2(total):
    input_set = file_to_set('input_day1_2.txt')
    for count_outer, val_outer in enumerate(input_set):
        for _, val_inner in enumerate(input_set, start=count_outer + 1):
            val_calc = total - val_outer - val_inner
            if val_calc in input_set:
                return val_outer * val_inner * val_calc


def main():
    NUM = 2020
    print(day_1(NUM))
    print(day_1_2(NUM))


if __name__ == '__main__':
    main()