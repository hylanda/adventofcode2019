f = open("Day2/input2.txt", "r")
mat = []
line = f.readline()
mat = [int(x) for x in line.split(',')]
#replace to 1202
mat[1] = 12
mat[2] = 2
for num in range(0, mat.__len__(), 4):
    a, b, c = num + 1, num + 2, num + 3
    if mat[num] == 99:
        print(mat[0])
        exit()
    elif mat[num] == 1:
        mat[mat[c]] = mat[mat[a]] + mat[mat[b]]
    elif mat[num] == 2:
        mat[mat[c]] = mat[mat[a]] * mat[mat[b]]
    else:
        print("sumting wong")
        exit(99)
f.close()


