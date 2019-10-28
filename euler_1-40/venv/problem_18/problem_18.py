f = open("data.txt","r")

data = []
for line in f:
    data.append((line.strip()).split(" "))

print(data)
print(len(data))

index = 0
sum = int(data[0][0])
for row in range(len(data)-1):
    print(data[row][index],row,index)
    x = data[row + 1][index]
    y = data[row + 1][index + 1]
    if x > y:
        index = index
    else:
        index += 1
    sum += int(data[row][index])

print(data[3][index],row,index)
x = data[3][index]
y = data[3][index + 1]
if x > y:
    index = index
else:
    index += 1
sum += int(data[-1][index])

print("Sum",sum)