def isPalindrome(str1):
    if len(str1) <= 1:
        return True
    else:
        return str1[0] == str1[-1] and isPalindrome(str1[1:-1])

num1 = 100
num2 = 100
largest = 0

while True:
    numi = num1 * num2
    if isPalindrome(str(numi)):
        if numi > largest:
            largest = numi
    num1 += 1
    if num1 == 1000:
        num1 = 100
        num2 += 1
    if num2 == 1000:
        break

print(largest)