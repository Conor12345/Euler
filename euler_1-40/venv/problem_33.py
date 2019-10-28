import fractions

for numerator in range(10,100):
    for denominator in range(10,100):
        if numerator / denominator < 1 and (numerator % 11) + (denominator % 11) != 0 and numerator % 10 != 0:
            common = None
            dict1 = {}
            for i in str(numerator):
                if i in dict1:
                    dict1[i] += 1
                else:
                    dict1[i] = 1
            for i in str(denominator):
                if i in dict1:
                    dict1[i] += 1
                else:
                    dict1[i] = 1
            for i in dict1:
                if dict1[i] == 2 and i != 0:
                    common = i
                    if common != None and len(str(numerator)) == 2 and len(str(denominator)) == 2:
                        if str(numerator)[0] == str(common):
                            numerator = int(str(numerator)[1])
                        else:
                            numerator = int(str(numerator)[0])
                        if str(denominator)[0] == str(common):
                            denominator = int(str(denominator)[1])
                        else:
                            denominator = int(str(denominator)[0])
            print(numerator,denominator)
            #print(common)