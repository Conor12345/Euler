import re
from time import time

str1 = r"11"
for i in range(2, 20):
    str1 += "|" + str(11 ** i)
print(str1)
elevenRegex = re.compile(str1)

def findElevens(number): # True if has elevens # False if no elevens
    regex = elevenRegex.search(str(number))
    if regex is None:
        return False
    else:
        return True

maximum = 10 ** 2
current = 1
prev = [0,0] # index, number
elevens = []

while True:
    if not findElevens(current):
        prev[0] += 1
        prev[1] = current
    else:
        elevens.append(current)
    current += 1
    if prev[0] >= maximum:
        print(prev[1])
        break

print(len(elevens))