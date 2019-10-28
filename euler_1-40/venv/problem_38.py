from functiones import *

largest = 0
num = 1
pan = ""

while True:
    multiple = 2
    pan = ""
    pan += str(num)
    while len(pan) < 9:
        pan += str(num * multiple)
        multiple += 1
    num += 1

    if len(pan) == 9 and isPandigital(pan,9):
        if int(pan) > largest:
            largest = int(pan)
    print(pan, largest)
