import re


def file_to_set(file):
    with open(file) as f:
        return set(int(val.strip()) for val in f.readlines())


def file_to_password_list(file):
    with open(file) as f:
        return [Password.string_init(line.strip()) for line in f.readlines()]


def file_to_matrix(file):
    matrix = []
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            matrix.append([char for char in line.strip()])
    return matrix


def file_to_passport(file):
    with open(file) as f:
        passport_lines = f.read().split('\n\n')
        return [Passport(line) for line in passport_lines]


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


def day_2():
    return sum([pw.is_valid() for pw in file_to_password_list('input_day2.txt')])


def day_2_2():
    return sum([pw.is_valid2() for pw in file_to_password_list('input_day2_2.txt')])


def day_3(right: int, bottom: int):
    count = 0
    matrix = file_to_matrix('input_day_3_1.txt')

    for i, row in enumerate(matrix):
        if i % bottom == 0:
            if row[(i * right // bottom) % len(row)] == '#':
                count += 1
    return count


def day_4():
    return len([True for pw in file_to_passport('input_day_4.txt') if pw.is_valid()])


class Password:
    def __init__(self, password, character, min_amount, max_amount):
        self.password = password
        self.character = character
        self.min = int(min_amount)
        self.max = int(max_amount)

    def __str__(self):
        return f'min: {self.min}| max: {self.max}| char: {self.character}| password: {self.password} \n'

    def __repr__(self):
        return self.__str__()

    @classmethod
    def string_init(cls, input_string: str) -> 'Password':
        lst = input_string.split(' ')
        nums = lst[0].split('-')
        return cls(lst[2], lst[1][0], nums[0], nums[1])

    def is_valid(self):
        return self.min <= self.password.count(self.character) <= self.max

    def is_valid2(self):
        return (self.password[self.min - 1] == self.character) ^ (self.password[self.max - 1] == self.character)


def check_year(val: str, min_val, max_val):
    if val.isdigit() and min_val <= int(val) <= max_val:
        return True


class Passport:

    CHECK_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

    def __init__(self, init_string):
        self._data = {}
        for key_val in init_string.split():
            self._create_key_value(key_val)

    def _create_key_value(self, key_val):
        key_val = key_val.split(':')
        self._data[key_val[0]] = key_val[1]

    def is_valid(self):
        return len(self.__class__.CHECK_FIELDS - set(self._data.keys())) == 0

    def is_valid2(self):
        if self.is_valid():
            count = 0
            count += check_year(self._data['byr'], 1920, 2002)
            count += check_year(self._data['iyr'], 2010, 2020)
            count += check_year(self._data['eyr'], 2020, 2030)
            count += self._check_height()
            count += self._check_hair_color()
            count += self._check_eye_color()
            count += self._check_passport_id()
            return count == len(self.__class__.CHECK_FIELDS)

        return False

    def _check_height(self):
        data = self._data['hgt']
        num = int(data[:-2])
        unit = data[-2:]

        if unit == 'cm':
            return 150 <= num <= 193
        if unit == 'in':
            return 59 <= num <= 76
        return False

    def _check_hair_color(self):
        return re.fullmatch('#([a-f0-9]{6})', self._data['hcl'])

    def _check_eye_color(self):
        return self._data['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

    def _check_passport_id(self):
        return len(self._data['pid'] == 9) and self._data['pid'].isdigit()


if __name__ == '__main__':
    # NUM = 2020
    # # print(day_1(NUM))
    # # print(day_1_2(NUM))
    # # print(day_2())
    # print(day_2_2())
    # print(day_3(1, 2))
    # print(day_3(1, 1) * day_3(3, 1) * day_3(5, 1) * day_3(7, 1) * day_3(1, 2))
    # print(1 % 1)
    # print(1 % 2)
    # print(day_4())
    print(int('bla'))
