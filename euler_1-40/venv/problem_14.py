def sequence(start):
    list1 = [start]
    while list1[-1] != 1:
        #print(list1[-1])
        if list1[-1] % 2 == 1:
            list1.append((3 * list1[-1]) + 1)
        else:
            list1.append(0.5 * list1[-1])
    return len(list1)

largest = [0,0]

for i in range(1, 1000001):
    x = sequence(i)
    print(x, i)
    if x > largest[0]:
        largest[0] = x
        largest[1] = i

print(largest)