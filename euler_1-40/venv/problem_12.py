from functools import reduce

def factors(num):
    return set(reduce(list.__add__,
                      ([i,num//i] for i in range(1,int(num ** 0.5) + 1) if num % i == 0)))

currentAdd = 2
currentTri = 1

while len(factors(currentTri)) < 501:
    x = factors(currentTri)
    print(currentTri, len(x), x)
    currentTri += currentAdd
    currentAdd += 1

print(currentTri)

