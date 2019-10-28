from itertools import permutations

data = list(permutations(range(10),10))
data.sort()
print(data[999999])