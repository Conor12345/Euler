pentagonalNums = []
for n in range(1,10001):
    pentagonalNums.append(n * (3 * n - 1) / 2)

#print(pentagonalNums)
smallestDif = 100000

for high in pentagonalNums:
    for low in pentagonalNums:
        if high != low:
            summ = high + low
            diff = abs(high - low)
            if summ in pentagonalNums and diff in pentagonalNums:
                if diff < smallestDif:
                    smallestDif = diff
            print(high,low,smallestDif,summ,diff)

