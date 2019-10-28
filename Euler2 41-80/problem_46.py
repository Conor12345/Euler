from functiones import getPrimesBelowN

allPrimes = getPrimesBelowN()
print(allPrimes)
twicesquare = []

for i in range(10):
    twicesquare.append(2 * (i ** 2))

primes = []
notprimes = []

for i in range(1, len(getPrimesBelowN())):
    if not allPrimes[i]:
        notprimes.append(i)
    else:
        primes.append(i)

