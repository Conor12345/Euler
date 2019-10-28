data = []
f = open("data.txt","r")
for line in f:
    data.append(line.strip().split(","))
size = len(data)

def printData():
    for i in data:
        print(*i)

for y in range(0, len(data) - 1):
    for x in range(0, len(data) - 1):
        data[y][x] = int(data[y][x])

printData()

class Node:
    def __init__(self, value):
        self.value = value
        self.down = None
        self.right = None

    def addRight(self, value):
        if self.right is None:
            self.right = Node(value)
        else:
            self.right.addRight(value)

    def addDown(self, value):
        if self.down is None:
            self.down = Node(value)
        else:
            self.down.addDown(value)

nowd = Node(data[0][0])
print(nowd)

for y in range(0, len(data) - 1):
    for x in range(0, len(data[0]) - 1):
        if y == 0:
            if x != 0:
                nowd.addRight(data[y][x])
        elif x == 0:
            nowd.addDown(data[y][x])
        else:
            pass

print("owo")
