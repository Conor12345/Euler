import primefactors

print(len(set(primefactors.factorize(644))))

current = 3
count = 0
num = 4

while True:
    if len(set(primefactors.factorize(current))) == num:
        count += 1
    else:
        count = 0
    if count == num:
        print(current)
        break

    current += 1