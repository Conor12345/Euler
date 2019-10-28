ranger = 1000001

pentagonalNums = []
for n in range(1,ranger):
    pentagonalNums.append(n * (3 * n - 1) / 2)

hexagonalNums = []
for n in range(1, ranger):
    hexagonalNums.append(n * (2 * n - 1))

for n in range(44410, ranger):
    num = (n * (n+1)) / 2
    if n % 10 == 0:
        print(n, num)
    if num in pentagonalNums and num in hexagonalNums:
        print("owow",num,"---------------")
        x = input("onosanofs")