f = open("data.txt", "r")

data = []
for line in f:
    data.append(line.strip())

sum = 0
for i in data:
    sum += int(i)

print(sum)