def file_to_matrix(file):
    matrix = []
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            matrix.append([char for char in line.strip()])
    return matrix


def day_3(right: int, bottom: int):
    count = 0
    matrix = file_to_matrix('2022/day3/input_day_3_1.txt')

    for i, row in enumerate(matrix):
        if i % bottom == 0:
            if row[(i * right // bottom) % len(row)] == '#':
                count += 1
    return count
