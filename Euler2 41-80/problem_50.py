from functiones import getPrimesBelowN

allPrimes = getPrimesBelowN(1000)
primes = []
for i in range(0,len(allPrimes)):
    if allPrimes[i]:
        primes.append(i)

altPrimes = primes
altPrimes.reverse()

for prime in altPrimes:
    for start in range(0,len(primes)):
        current = prime
        index = start
        while current > 0:
            current -= primes[index]
        if current == 0:
            print(prime, index)