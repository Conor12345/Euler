from functools import reduce

def factors(num):
    return set(reduce(list.__add__,
                      ([i,num//i] for i in range(1,int(num ** 0.5) + 1) if num % i == 0)))

def de(num):
    return sum(sorted(factors(num))[:-1])

print(de(28))
print(de(284))
print(de(de(220)))

list1 = []
for num in range(2,10001):
    a = de(num)
    b = de(a)
    if num == de(de(num)) and a != b:
        list1.append(num)

print(list1)
print(sum(list1))