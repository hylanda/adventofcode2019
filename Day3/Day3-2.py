#Messy, non-pythonic attempt at linear algebra to solve day 3

def create_line_segment_points(inputs):
    x = 0
    y = 0
    points = [(0, 0)]
    for d in range(inputs.__len__()):
        direction = inputs[d][0]
        if direction == 'U':
            y += float(inputs[d][1:])
        elif direction == 'D':
            y -= float(inputs[d][1:])
        elif direction == 'L':
            x -= float(inputs[d][1:])
        else:
            x += float(inputs[d][1:])
        points.append((x, y))
    return points


def intersect(p1, p2, q1, q2):
    x1, x2, x3, x4 = p1[0], p2[0], q1[0], q2[0]
    y1, y2, y3, y4 = p1[1], p2[1], q1[1], q2[1]
    ta1, ta2 = (y3 - y4) * (x1 - x3) + (x4 - x3) * (y1 - y3), (x4 - x3) * (y1 - y2) - (x1 - x2) * (y4 - y3)
    tb1, tb2 = (y1 - y2) * (x1 - x3) + (x2 - x1) * (y1 - y3), (x4 - x3) * (y1 - y2) - (x1 - x2) * (y4 - y3)
    if ta2 > 0 and tb2 > 0:
        ta = ta1 / ta2
        tb = tb1 / tb2
        if 0 <= ta <= 1 and 0 <= tb <= 1:
            return x1 + ta * (x2 - x1), y1 + ta * (y2 - y1)
            # return x3+tb*(x4-x3), y3+tb*(y4-y3)
    return 0, 0


f = open("input3.txt", "r")
line = f.readline()
p = [str(x) for x in line.split(',')]
line = f.readline()
q = [str(x) for x in line.split(',')]

w1 = create_line_segment_points(p)
w2 = create_line_segment_points(q)
inter = []
for i in range(w1.__len__() - 1):
    for j in range(w2.__len__() - 1):
        tup = intersect(w1[i], w1[i + 1], w2[j], w2[j + 1])
        if tup[0] + tup[1] > 0:
            inter.append(tup)
for (x, y) in inter:
    print(x + y)
f.close()
