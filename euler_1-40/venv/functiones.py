from functools import reduce
import primefactors

def pFactors(x):
    return primefactors.factorize(x)

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