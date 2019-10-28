def pythag(a,b):
    return (((a ** 2) + (b ** 2)) ** 0.5)

a = 2
b = 2

while True:
    c =  pythag(a,b)
    if a + b + c == 1000 and c % 1 == 0:
        print(a,b,c)
        break
    a += 1
    if a == 999:
        a = 2
        b += 1


