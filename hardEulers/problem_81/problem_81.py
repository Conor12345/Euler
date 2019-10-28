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

def addDood(Node, y, x):
    if y + 1 < size and x + 1 < size:
        Node.child1 = N(y + 1, x, Node)
        addDood(Node.child1, y + 1, x)
        Node.child2 = N(y, x + 1, Node)
        addDood(Node.child2, y, x + 1)
    elif y + 1 < len(data) and x + 1 >= len(data[0]):
        Node.child1 = N(y + 1, x, Node)
        addDood(Node.child1, y + 1, x)
    elif y + 1 >= len(data) and x + 1 < len(data[0]):
        Node.child2 = N(y, x + 1, Node)
        addDood(Node.child2, y, x + 1)
    else:
        return None

def sumMini(root):
    if root.child1 is None and root.child2 is None:
        return root.value
    elif root.child1 is None:
        return root.value + sumMini(root.child2)
    elif root.child2 is None:
        return root.value + sumMini(root.child1)
    else:
        return root.value + mini(sumMini(root.child1), sumMini(root.child2))

def mini(num1, num2):
    if num1 is None and num2 is None:
        return 0
    elif num1 is None:
        return num2
    elif num2 is None:
        return num1
    else:
        return min(num1, num2)

class N:
    def __init__(self, ypos, xpos, parent):
        self.value = int(data[ypos][xpos])
        self.child1 = None
        self.child2 = None
        self.parent = parent

rewt = N(0, 0, None)
addDood(rewt, 0, 0)

print(sumMini(rewt))
print("owo")