def possible(x, y):
    for sx, sy, d in sensors:
        if abs(x - sx) + abs(y - sy) <= d and (x, y) not in beacons:
            return False
    return True


def p1():
    ct = 0
    y = 2_000_000
    for x in range(min(x - d for x, _, d in sensors), max(x + d for x, _, d in sensors)):
        if not possible(x, y) and (x, y) not in beacons:
            ct += 1
    return ct


def p2(sensors):
    for sx, sy, d in sensors:
        for dx in range(d + 2):
            dy = (d + 1) - dx
            for mx, my in [(-1, 1), (1, -1), (-1, -1), (1, 1)]:
                x, y = sx + (dx * mx), sy + (dy * my)
                if not (0 <= x <= 4_000_000 and 0 <= y <= 4_000_000):
                    continue
                if possible(x, y):
                    return x * 4_000_000 + y



def main():

    # data = open("input.txt").read().strip()
    # sensors, beacons = set(), set()
    # for line in data.split("\n"):
    #     parts = line.split()
    #     sx, sy = int(parts[2][2:-1]), int(parts[3][2:-1])
    #     bx, by = int(parts[8][2:-1]), int(parts[9][2:])
    #     d = abs(sx - bx) + abs(sy - by)
    #     sensors.add((sx, sy, d))
    #     beacons.add((bx, by))
    # print(f"Part 1: {p1()}")
    # print(f"Part 2: {p2(sensors)}")

    y = 0
    for x in range(4_000_000):
        for y in range(4_000_000):
            y = x
    print(y)

main()
