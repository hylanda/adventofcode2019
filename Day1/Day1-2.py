

import math


def fuel(x):
    y = math.floor(x/3)-2
    if y > 0:
        return x+fuel(y)
    else:
        return x

f = open("input.txt", "r")
summation = 0
flines = f.readlines()
for line in flines:
    y = fuel(math.floor(int(line)/3)-2)
    summation = summation + y
print(summation)
f.close()

