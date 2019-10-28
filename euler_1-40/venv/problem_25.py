fibs = [1, 1]
index = 2

while len(str(fibs[-1])) != 1000:
    fibs.append(fibs[-1] + fibs[-2])
    index += 1

print(fibs[-1],index)