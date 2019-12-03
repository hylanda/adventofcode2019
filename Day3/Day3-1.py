# I wish this was more elegant but it got the right answers
lines = open("input3.txt", "r").readlines()
grid = [{}, {}]
for i in range(lines.__len__()):
    row = lines[i]
    x, y = 0, 0
    length = 0
    for wire in row.split(','):
        p, q = 0, 0
        if wire[0] == "R":
            p = 1
        elif wire[0] == "L":
            p = -1
        if wire[0] == "U":
            q = 1
        elif wire[0] == "D":
            q = -1
        for _ in range(int(wire[1:])):
            x += p
            y += q
            length += 1
            if (x, y) not in grid[i]:
                grid[i][(x, y)] = length
inter = set(grid[0]) & set(grid[1])
print(min([abs(x) + abs(y) for (x, y) in inter]))
print(min([grid[0][p] + grid[1][p] for p in inter]))
