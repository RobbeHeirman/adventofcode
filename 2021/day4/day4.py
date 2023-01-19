import re


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


def file_to_passport(file):
    with open(file) as f:
        passport_lines = f.read().split('\n\n')
        return [Passport(line) for line in passport_lines]


def day_4():
    return len([True for pw in file_to_passport('input_day_4.txt') if pw.is_valid()])


if __name__ == "__main__":
    day_4()
