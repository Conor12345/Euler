import itertools
import functiones

data = itertools.permutations([9,8,7,6,5,4,3,2,1])
#primes = functiones.getprimes(987654322)
#print(primes[7])



for i in data:
    num = ""
    for j in i:
        num += str(j)
    num = int(num)
    print(num)
    if functiones.isPrimeFast(num):
        print(num)
        break