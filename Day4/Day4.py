def check_number_one(num):
    stack = []
    ascending = 1
    double = 0
    while num > 0:
        stack.append(num % 10)
        num = num / 10
    for i in range(stack.__len__()-1):
        if stack.count(stack[i]) >= 2:
            double = 1
        if stack[i] < stack[i+1]:
            ascending = 0
    return ascending and double


def check_number_two(num):
    stack = []
    ascending = 1
    double = 0
    while num > 0:
        stack.append(num % 10)
        num = num / 10
    for i in range(stack.__len__()-1):
        if stack.count(stack[i]) == 2:
            double = 1
        if stack[i] < stack[i+1]:
            ascending = 0
    return ascending and double


low, high = 134564, 585159
count_one = 0
count_two = 0
for x in range(low, high):
    count_one += check_number_one(x)
    count_two += check_number_two(x)
print count_one
print count_two
