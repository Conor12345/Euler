current = 230000000

while True:
    flag = False
    for i in range(1,21):
        if current % i != 0:
            flag = True
    if flag == False:
        print(current)
        break
    print(current)
    current += 1