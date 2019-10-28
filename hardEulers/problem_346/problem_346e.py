def decimalConverter(n, base):
    length = len(str(n))
    return (base ** length - 1) // (base - 1)

data = {}
maxNum = 10 ** 12
base = 2
outList = []

while True:
    current = 1
    n = 1
    while True:
        if current not in data:
            data[current] = 1
        else:
            data[current] += 1
            if data[current] == 2 and current < maxNum:
                outList.append(current)
        current += base ** n
        n += 1
        if current > maxNum:
            break
    base += 1
    if base >= maxNum:
        break
    if base % 1000 == 0:
        print((base / maxNum) * 100)
print(sum(outList))