import functiones

def abundant(num):
    x = list(functiones.factors(num))
    if (num ** 0.5) % 1 == 0:
        x.append(int(num ** 0.5))
    return sum(sorted(x)[:-1]) > num

def addup(List, K):
    front = 0
    back = len(List) - 1
    while front < back:
        sum = List[front] + List[back]
        if sum == K:
            return True
        elif sum < K:
            front += 1
        elif sum > K:
            back -= 1
    return False

print(abundant(49))

abundants = []
for i in range(1,28124):
    if abundant(i):
        abundants.append(i)

sum = 0
for i in range(1,21000):
    if not addup(abundants,i):
        sum += i
    print(i, sum)

print(sum)