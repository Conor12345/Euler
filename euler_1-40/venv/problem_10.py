import primefactors

sum = 0
for num in range(2,2000000):
    if len(primefactors.factorize(num)) < 2:
        sum += num
        print(num)
print(sum)