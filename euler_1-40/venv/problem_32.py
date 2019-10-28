from functiones import *

a = 1
b = 1
outList = []

while True:
    c = a * b#
    flag = True
    if isPandigital(str(a) + str(b) + str(c),9):
        for item in outList:
            if c == item[2]:
                flag = False
        if flag:
            outList.append([a,b,c])
    a += 1
    if a > 10000:
        b += 1
        a = 1
    sum = 0
    for i in outList:
        sum += i[2]
    print(a,b,sum,outList)