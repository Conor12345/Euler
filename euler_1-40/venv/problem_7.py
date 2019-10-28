import primefactors

def isPrimeNo(num1):
    if len(primefactors.factorize(num1)) == 1:
        return True
    else:
        return False

primeNo = 0
currentNum = 1

while True:
    if isPrimeNo(currentNum):
        primeNo += 1
        print(primeNo, currentNum)
    if primeNo == 10001:
        print(currentNum)
        break
    currentNum += 1