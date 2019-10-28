data = "0."
num = 1

while len(data) < 2000000:
    data += str(num)
    num += 1

data = data[2:]

location = 1
out = 1
while location < 10000000:
    print(location)
    out = out * int(data[location - 1])
    location = location * 10

print(out)
print("owo")