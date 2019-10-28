from functiones import factors


def isPrime(num):
    if num != 0:
        return len(factors(int(num))) <= 2
    else:
        return False

def eulerTest(a, b, n):
    x = int((n ** 2) + (a * n) + b)
    if x < 0:
        return -int((n ** 2) + (a * n) + b)
    else:
        return int((n ** 2) + (a * n) + b)

print(isPrime(eulerTest(1,41,41)))
largest = [0,0,0]
for a in range(-1000,1001):
    for b in range(-1000,1001):
        num = 0
        while isPrime(eulerTest(a,b,num)):
            num += 1
        if num != 0:
            if num > largest[2]:
                largest = [a,b,num]
        print(a,b,num)
print(largest)

