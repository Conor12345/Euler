sum = 0

for num in range(1,1000001):
    x = str(bin(num))[2:]
    if str(num) == str(num)[::-1] and x == x[::-1]:
        sum += num

print(sum)