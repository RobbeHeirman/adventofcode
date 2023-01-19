

def position_changer(input_: str, pos_tuple: (int, int)) -> (int, int):
    direction, movement = input_.split()
    movement = int(movement)
    forward = pos_tuple[0]
    depth = pos_tuple[1]
    if direction == 'forward':
        forward += movement
    elif direction == 'up':
        depth -= movement
    elif direction == "down":
        depth += movement

    return forward, depth


def second_position_changer(input_: str, pos_tuple: (int, int))-> (int, int):

    direction, movement = input_.split()
    movement = int(movement)
    pos = pos_tuple[0]
    depth = pos_tuple[1]
    aim = pos_tuple[2]

    if direction == 'forward':
        pos += movement
        depth += aim * movement
    elif direction == 'up':
        aim -= movement
    elif direction == "down":
        aim += movement

    return pos, depth, aim





def ex1():
    with open('../../../adventofcode/2021/day2.txt') as f:
        pos = (0, 0)
        for line in f:
            pos = position_changer(line[:-1], pos)

        print(pos[0] * pos[1])


def ex2():
    with open('../../../adventofcode/2021/day2.txt') as f:
        pos = (0, 0, 0)
        for line in f:
            pos = second_position_changer(line[:-1], pos)

        print(pos[0] * pos[1])


if __name__ == "__main__":
    ex2()