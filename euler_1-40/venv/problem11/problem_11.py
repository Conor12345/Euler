f = open("data.txt","r")
data = []
for line in f:
    data.append(line.strip().split(" "))

for i in range(20):
    for j in range(20):
        data[i][j] = int(data[i][j])

print(data)
largest = 0

# horizonal
for ar in data:
    for pos in range(len(ar) - 3):
        current = 1
        for i in range(4):
            current = current * ar[pos + i]
        #print(current)
        if current > largest:
            largest = current

# vertical needs redoing
for width in range(20):
    for height in range(17):
        current = 1
        for i in range(3):
            current = current * data[width][height + i]
        #print(current)
        if current > largest:
            largest = current

# diagonal (up left)
for width in range(17):
    for height in range(17):
        current = 1
        current = current * data[width][height]
        current = current * data[width + 1][height - 1]
        current = current * data[width + 2][height - 2]
        current = current * data[width + 3][height - 3]
        if current > largest:
            largest = current

# diagonal (down left)
for width in range(17):
    for height in range(17):
        current = 1
        current = current * data[width][height]
        current = current * data[width + 1][height + 1]
        current = current * data[width + 2][height + 2]
        current = current * data[width + 3][height + 3]
        if current > largest:
            largest = current


print(largest)