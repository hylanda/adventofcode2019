f = open("Day1/input.txt", "r")
summation = 0
for line in f.readlines():
    summation += int(int(line) / 3) - 2
print(summation)
f.close()
