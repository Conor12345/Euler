data = []

for a in range(2,101):
    for b in range(2,101):
        x = a ** b
        if x not in data:
            data.append(x)

print(len(sorted(data)))