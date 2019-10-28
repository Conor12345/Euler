from functiones import *

current = 8
outList = []

while len(outList) < 11:
    allPrime = True
    for i in truncateleft(current):
        if not isprime(i):
            allPrime = False
    for i in truncateright(current):
        if not isprime(i):
            allPrime = False
    if allPrime:
        outList.append(current)
    print(outList,current)
    current += 1

print(sum(outList))