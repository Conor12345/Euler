from functools import reduce

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def abundant(list1):
    list1 = list(list1)
    list1 = sorted(list1)
    val = list1[-1]
    del list1[-1]
    sum = 0
    for i in list1:
        sum += i
    if sum > val:
        return 1
    elif sum < val:
        return -1
    else:
        return 0


def addup(list):
    sums = [0] * 28124
    for x in range(0,len(list)):
        for y in range(x,len(list)):
            sumOfAbundants = list[x] + list[y]
            if sumOfAbundants <= 28123:
                if sums[sumOfAbundants] == 0:
                    sums[sumOfAbundants] = sumOfAbundants
    total = 0
    for x in range(0, len(sums)):
        if sums[x] == 0:
            total += x
    return total

abundantlist = []
deficientlist = []
perfectnumberlist = []

for i in range(1,28123):
    vall = abundant(factors(i))
    if vall == 1:
        abundantlist.append(i)
    elif vall == 0:
        perfectnumberlist.append(i)
    elif vall == -1:
        deficientlist.append(i)


print(len(abundantlist),abundantlist)
print(len(deficientlist),deficientlist)
print(len(perfectnumberlist),perfectnumberlist)

print(addup(abundantlist))