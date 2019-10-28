data = {}

def decimalConverter(n, b):
    mulitplier = 1
    total = 0
    n = str(n)
    for i in range(len(n) - 1, -1, -1):
        total += int(n[i]) * mulitplier
        mulitplier = mulitplier * b
    return total

current = "1"
while True:
    print(current)
    for base in range(3, 10 ** 3):
        print(base)
        num = decimalConverter(int(current), base)
        if num in data:
            data[num] += 1
        else:
            data[num] = 1
    current += "1"
    if len(current) > 45:
        break

sum = 0
for i in data:
    if data[i] > 1:
        if i < 10 ** 3:
            print(i)
print(sum)