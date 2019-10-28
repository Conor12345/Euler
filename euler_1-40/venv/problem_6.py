sum1 = 0
sum2 = 0

for i in range(1,101):
    sum1 += i ** 2

for i in range(1,101):
    sum2 += i

print(- sum1 + (sum2 ** 2))