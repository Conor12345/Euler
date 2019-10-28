import math
import time
start = time.process_time()
def printSpriral(data):
    for i in data:
        print(*i)

n = 1001
data = []
for i in range(n):
    list1 = []
    for j in range(n):
        list1.append(0)
    data.append(list1)

row = math.floor(n/2)
col = math.floor(n/2)
data[row][col] = 1

col += 1
data[row][col] = 2
row += 1
data[row][col] = 3
#printSpriral(data)
print("")
direction = "left"

for num in range(4, (n ** 2) + 1):
    if direction == "left":
        col -= 1
        if data[row - 1][col] != 0:

            data[row][col] = num
        else:
            data[row][col] = num
            direction = "up"
    elif direction == "up":
        row -= 1
        if data[row][col + 1] != 0:
            data[row][col] = num
        else:
            data[row][col] = num
            direction = "right"
    elif direction == "right":
        col += 1
        if data[row + 1][col] != 0:
            data[row][col] = num
        else:
            data[row][col] = num
            direction = "down"
    elif direction == "down":
        row += 1
        if data[row][col - 1] != 0:
            data[row][col] = num
        else:
            data[row][col] = num
            direction = "left"
    #printSpriral(data)     
#printSpriral(data)

sum = 0
row = 0
col = 0
while row != n:
    sum += data[row][col]
    row += 1
    col += 1

row = n - 1
col = 0

while row != -1:
    sum += data[row][col]
    row -= 1
    col += 1

print(sum - 1)

print("Time taken:", time.process_time() - start)