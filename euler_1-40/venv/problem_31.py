current = [0,0,0,0,0,0,0,1] # 0 = 1p, 1 = 2p, 2 = 5p, 3 = 10p, 4 = 20p, 5 = 50p, 6 = £1, 7 = £2

def isTooBig(values,total):
    sum = 0
    sum += values[0]
    sum += values[1] * 2
    sum += values[2] * 5
    sum += values[3] * 10
    sum += values[4] * 20
    sum += values[5] * 50
    sum += values[6] * 100
    sum += values[7] * 200
    if sum == total:
        return True
    else:
        return False

permutations = 0

penny = 0 # 1 permutations
twopenny = 0 # 2 permutations
fivepenny = 0 # 4 permutations
tenpen = 0 # 11 permutations
twentypen = 0 # 41 permutations
fiftypen = 0 # 451  permutations
pound = 0
twopound = 0

for penny in range(0,201):
    for twopenny in range(0,101):
        for fivepenny in range(0,41):
            for tenpen in range(0, 21):
                for twentypen in range(0,11):
                    #for fiftypen in range(0,5):
                        #for pound in range(0,3):
                            print([penny,twopenny,fivepenny,tenpen,twentypen,fiftypen,pound,0])
                            if isTooBig([penny,twopenny,fivepenny,tenpen,twentypen,fiftypen,pound,0],100):
                                permutations += 1

print(permutations )