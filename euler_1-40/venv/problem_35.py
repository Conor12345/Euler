from __future__ import generators
from functiones import *


def returnCircs(num):
    list1 = [num]
    while len(list1) != len(str(list1[0])):
        list1.append(int(str(list1[-1])[1:] + str(list1[-1])[0]))
        #print(list1)
    return list1

goodnums = []
print(returnCircs(1932))

def eratosthenes():
	'''Yields the sequence of prime numbers via the Sieve of Eratosthenes.'''
	D = {}  # map composite integers to primes witnessing their compositeness
	q = 2   # first integer to test for primality
	while 1:
		if q not in D:
			yield q        # not marked composite, must be prime
			D[q*q] = [q]   # first multiple of q not already marked
		else:
			for p in D[q]: # move each witness to its next multiple
				D.setdefault(p+q,[]).append(p)
			del D[q]       # no longer need D[q], free memory
		q += 1

def getPrimesBelowN(n=1000000):
    """Get all primes below n with the sieve of Eratosthenes.
    @return: a list 0..n with boolean values that indicate if
             i in 0..n is a prime.
    """
    from math import ceil
    primes = [True] * n
    primes[0] = False
    primes[1] = False
    primeList = []
    roundUp = lambda n, prime: int(ceil(float(n) / prime))
    for currentPrime in range(2, n):
        if not primes[currentPrime]:
            continue
        primeList.append(currentPrime)
        for multiplicant in range(2, roundUp(n, currentPrime)):
            primes[multiplicant * currentPrime] = False
    return primes

primes = getPrimesBelowN()
#print(primes)

for num in range(1,1000000):
    data = returnCircs(num)
    flag = True
    for i in str(num):
        if i == "0":
            flag = False
    for i in data:
        if primes[i] == False:
            flag = False
    if flag:
        goodnums.append(num)
    print(data,flag)
print(len(goodnums),goodnums)