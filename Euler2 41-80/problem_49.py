from functiones import getPrimesBelowN

allPrimes = getPrimesBelowN(100000)

print(sorted(set(list(str(4187)))))

for i in range(1000,10001):
    if allPrimes[i]:
        for add in range(1,4500):
            if allPrimes[i + add] and allPrimes[i + add + add] and i + add + add < 10000:
                if sorted(set(list(str(i)))) ==  sorted(set(list(str(i + add)))) and sorted(set(list(str(i + add + add)))) ==  sorted(set(list(str(i + add)))):
                    print(i, i + add, i + add + add)