def raiseDigitsTo(num, power):
    sum = 0
    for digit in str(num):
        sum += (int(digit) ** power)
    return sum

power = 5
sum = 0
current = 2

while True:
    if raiseDigitsTo(current, power) == current:
        sum += current
    current += 1
    print(sum)