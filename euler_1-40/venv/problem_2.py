fib = [1, 2]

while fib[-1] < 4000000:
    fib.append(fib[-2] + fib[-1])

print(fib)

count = 0
for i in fib:
    if i % 2 == 0:
        count += i

print(count)