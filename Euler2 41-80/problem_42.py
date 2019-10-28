triangleNumbers = []

for num in range(1,1001):
    triangleNumbers.append(int(0.5 * num * (num + 1)))
print(triangleNumbers)

f = open("data.txt","r")
for line in f:
    data = (line.strip()).split(",")
data2 = []
for word in data:
    data2.append(word[1:-1])
print(data2)

count = 0
for triNum in data2:
    sum = 0
    for letter in triNum:
        sum += ord(letter) - 64
    if sum in triangleNumbers:
        count += 1
print(count)