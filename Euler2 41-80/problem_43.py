from itertools import permutations

data = list(permutations([0,1,2,3,4,5,6,7,8,9]))
#data = [[1,4,0,6,3,5,7,2,8,9]]
divisors = [2,3,5,7,11,13,17]
goodnums = []

for num in data:
    flag = True
    for i in range(7):
        current = ""
        for j in range(1,4):
            current += str(num[i + j])
        current = int(current)
        if current % divisors[i] != 0:
            flag = False
            break
    if flag:
        goodnums.append(num)
    print(goodnums)

sumi = 0
for goodnum in goodnums:
    num = ""
    for i in goodnum:
        num += str(i)
    sumi += int(num)

print(sumi)