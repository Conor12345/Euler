f = open("data.txt","r")

for line in f:
    data = line.split(",")

data.sort()
for i in range(len(data)):
    data[i] = data[i][1:-1]

sum = 0
for nameNum in range(len(data)):
    print(data[nameNum])
    tempSum = 0
    for letter in data[nameNum]:
        tempSum += (ord(letter) - 64)
    sum += tempSum * (nameNum + 1)

print(sum)