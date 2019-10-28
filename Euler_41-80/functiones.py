from __future__ import generators
from functools import reduce
import math

def factors(n):
    if n != 0:
        return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    else:
        return []

def isprime(n):
    if len(factors(n)) == 2:
        return True
    return False

def concatanate(list):
    string = ""
    for i in list:
        string += str(i)
    return string

def truncateleft(num):
    string = str(num)
    length = len(string)
    listofvals = []
    for i in range(length):
        listofvals.append(int(string[i:]))
    return listofvals

def truncateright(num):
    string = str(num)
    length = len(string)
    listofvals = []
    listofvals.append(int(string))
    for i in range(1, length):
        listofvals.append(int(string[:-i]))
    return listofvals

def isPandigital(num, n):
    x = sorted(list(str(num)))
    flag = False
    if len(str(num)) != n:
        return False
    for i in range(1, n+1):
        if int(x[i - 1]) != i:
            flag = True
    if flag:
        return False
    else:
        return True

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

def getprimes(n):
    A = [True for x in range(n)]
    for i in range(2, int(math.sqrt(n)) + 1):
        if A[i]:
            for j in range(i ** 2, n, i):
                A[j] = False
    return A

def isPrimeFast(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True