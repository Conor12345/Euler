from math import log, ceil

max = 10 ** 3

def baseCalc(num, base):
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        maxcol = ceil(log(num, base))
        data = []
        for power in range(maxcol - 1, -1, -1):
            data.append([base ** power , 0])

        current = num
        for pair in data:
            while True:
                if current - pair[0] >= 0:
                    current -= pair[0]
                    pair[1] += 1
                else:
                    break

        val = ""
        for i in data:
            if int(i[1]) < 10:
                val += str(i[1])
            else:
                val += "9"
        return int(val)

def isRepunit(num, base):
    value = list(str(baseCalc(num, base)))
    if set(value) == {"1"}:
        return True
    else:
        return False

values = [1]
for num in range(1, max + 1):
    count = 0
    bases = []
    for base in range(2, num):
        print(num, base)
        if isRepunit(num, base):
            count += 1
            bases.append(base)
        if count > 1:
            values.append(num)
            break


print(sum(values))