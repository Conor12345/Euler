f = open("data.txt","r")

data = []
for line in f:
    data.append((line.strip()).split(" "))

for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j] = int(data[i][j])
print(data)

def compactor(data):
    for i in range(len(data[-1]) - 1):#
        print(data[-1][i], data[-1][i + 1],data[-2][i])
        botLeft = data[-1][i]
        botRight = data[-1][i + 1]
        top = data[-2][i]
        print(top + max(botLeft, botRight))
        data[-2][i] = top + max(botLeft, botRight)
    return data[:-1]

while len(data) != 1:
    data = compactor(data)
    for i in data:
        print(*i)
    print("\n")
    print("-" * 200)
    print("\n")

print("Final answer:",data[0][0])