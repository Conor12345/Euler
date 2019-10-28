def arrayGen(size):
    data = []
    for i in range(size):
        list1 = []
        for j in range(size):
            list1.append((i,j))
        data.append(list1)
    return data

def arrayPrint(array):
    for i in array:
        print(*i)

def BFS(array, n):
    queue = [(0,0)]
    visited = []
    while len(queue) > 0:
        v = queue.pop(0)
        visited.append(v)
        if v[0] != n-1:
            queue.append((v[0] + 1, v[1]))
        if v[1] != n-1:
            queue.append((v[0], v[1] + 1))
        print(len(queue),len(visited))
    return visited

n = 16
data = arrayGen(n)
arrayPrint(data)
data = BFS(data,n)

count = 0
print(data)
for i in data:
    if i == (n-1,n-1):
        count += 1
print(count)