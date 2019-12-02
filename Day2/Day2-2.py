def compute(line, noun, verb):
    mat = [int(x) for x in line.split(',')]
    mat[1] = noun
    mat[2] = verb
    for num in range(0, mat.__len__(), 4):
        a, b, c = num + 1, num + 2, num + 3
        if mat[num] == 99:
            return mat[0]
        elif mat[num] == 1:
            mat[mat[c]] = mat[mat[a]] + mat[mat[b]]
        elif mat[num] == 2:
            mat[mat[c]] = mat[mat[a]] * mat[mat[b]]
        else:
            exit(99)


f = open("Day2/input2.txt", "r")
line = f.readline()
for x in range(0, 99):
    for y in range(0, 99):
        if 19690720 == compute(line, x, y):
            print("noun is " + str(x))
            print("verb is " + str(y))
            print(100 * x + y)
            break
f.close()
