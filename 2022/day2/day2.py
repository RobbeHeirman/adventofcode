
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


def file_to_password_list(file):
    with open(file) as f:
        return [Password.string_init(line.strip()) for line in f.readlines()]


def day_2():
    return sum([pw.is_valid() for pw in file_to_password_list('2022/day2/input_day2.txt')])


def day_2_2():
    return sum([pw.is_valid2() for pw in file_to_password_list('2022/day2/input_day2_2.txt')])
