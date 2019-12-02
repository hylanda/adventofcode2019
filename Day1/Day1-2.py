
def fuel(x):
    y = int( x /3 ) -2
    if y > 0:
        return x+ fuel(y)
    else:
        return x


f = open("Day1/input.txt", "r")
summation = 0
for line in f.readlines():
    summation += fuel(int(int(line) / 3) - 2)
print(summation)
f.close()
