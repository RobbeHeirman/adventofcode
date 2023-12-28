mat = []

def sig(a):
    if a == 0:
        return 0
    else:
        return int(a/abs(a))

def dist(a, b):
    dx = b[0]-a[0]
    dy = b[1]-a[1]
    x = []
    y = []
    if dx == 0:
        x = []
    else:
        i = a[0]
        while i !=b[0]:
            i+=sig(dx)
            x.append(mat[i][a[1]])
    if dy == 0:
        y = []
    else:
        i = a[1]
        while i != b[1]:
            i+=sig(dy)
            y.append(mat[a[0]][i])

    return x.count("E")*1000000+len(x)-x.count("E") + y.count("E")*1000000+len(y)-y.count("E")


with open("input.txt","r") as f:
    for line in f:
        if line.count("#") == 0:
            mat.append(["E" for char in line.replace("\n", "")])
        else:
            mat.append([char for char in line.replace("\n", "")])

    mat = [list(x) for x in zip(*mat)]

    matt = []

    for line in mat:
        if line.count("#") == 0:
            matt.append(["E" for _ in line])
        else:
            matt.append(line)

    mat = matt

    locs = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == "#":
                locs.append((i, j))


    res = 0

    done = set()

    for a in locs:
        for b in locs:
            if (a, b) not in done and (b, a) not in done and a!=b:
                done.add((a, b))
                res += dist(a, b)

    print(res)