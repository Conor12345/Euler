from math import factorial

sum = 0
current = 3

while True:
    x = 0
    for i in str(current):
        x += factorial(int(i))
    if x == current:
        sum += current
        print(current)
    current += 1
    print(sum, current)