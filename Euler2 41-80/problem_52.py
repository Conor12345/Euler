#'sorted(set(list(str(i))))

current = 2


while True:
    for i in range(2,7):
        if sorted(set(list(str(current)))) != sorted(set(list(str(current * i)))):
            break
        print(current, current * 2)
        x = input(" ")
    current += 1