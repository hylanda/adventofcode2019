import math


f = open("input.txt", "r")
summation = 0
flines = f.readlines()
for line in flines:
    y = math.floor(int(line)/3)-2
    summation = summation + y
print(summation)
f.close()