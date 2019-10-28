data = {1}
maxi = 10 ** 12

for length in range(3, 50):
    base = 2
    while True:
        after = (base ** length - 1) // (base - 1)
        if after >= maxi or base >= after:
            break
        data.add(after)
        #print(length, base, after)
        #x = input(" ")
        base += 1
        if base % 10000 == 0:
            print((base / maxi) * 100)
print(sum(data))