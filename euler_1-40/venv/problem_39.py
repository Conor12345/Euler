def pythag(a,b):
    return ((a ** 2) + (b ** 2)) ** 0.5

rightTriangles = []
a = 1
b = 1
max = 1000

while b < max:
    arr = []
    c = pythag(a, b)
    if c % 1 == 0:
        arr = [a,b,int(c)]
        arr.sort()
    if arr not in rightTriangles and arr != []:
        rightTriangles.append(arr)
    a += 1
    if a == max:
        a = 1
        b += 1

dict1 = {}

for triangle in rightTriangles:
    x = sum(triangle)
    if x not in dict1:
        dict1[x] = 1
    else:
        dict1[x] += 1
print(dict1)

largest = [0,0]
for i in dict1:
    if dict1[i] > largest[0] and i <= 1000:
        largest[0] = dict1[i]
        largest[1] = i
print(largest)