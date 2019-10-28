def once(num):
    word = ''
    if num == '1':
        word = "One"
    if num == '2':
        word = "Two"
    if num == '3':
        word = "Three"
    if num == '4':
        word = "Four"
    if num == '5':
        word = "Five"
    if num == '6':
        word = "Six"
    if num == '7':
        word = "Seven"
    if num == '8':
        word = "Eight"
    if num == '9':
        word = "Nine"
    word = word.strip()
    return word

def ten(num):
    word = ''
    if num[0] == '1':
        if num[1] == '0':
            word = "Ten"
        if num[1] == '1':
            word = "Eleven"
        if num[1] == '2':
            word = "Twelve"
        if num[1] == '3':
            word = "Thirteen"
        if num[1] == '4':
            word = "Fourteen"
        if num[1] == '5':
            word = "Fifteen"
        if num[1] == '6':
            word = "Sixteen"
        if num[1] == '7':
            word = "Seventeen"
        if num[1] == '8':
            word = "Eighteen"
        if num[1] == '9':
            word = "Nineteen"
    else:
        text = once(num[1])
        if num[0] == '2':
            word = "Twenty"
        if num[0] == '3':
            word = "Thirty"
        if num[0] == '4':
            word = "Forty"
        if num[0] == '5':
            word = "Fifty"
        if num[0] == '6':
            word = "Sixty"
        if num[0] == '7':
            word = "Seventy"
        if num[0] == '8':
            word = "Eighty"
        if num[0] == '9':
            word = "Ninety"
        word = word + " " + text
    word = word.strip()
    return word

def hundred(num):
    word = ''
    text = ten(num[1:])
    if num[0] == '1':
        word = "One"
    if num[0] == '2':
        word = "Two"
    if num[0] == '3':
        word = "Three"
    if num[0] == '4':
        word = "Four"
    if num[0] == '5':
        word = "Five"
    if num[0] == '6':
        word = "Six"
    if num[0] == '7':
        word = "Seven"
    if num[0] == '8':
        word = "Eight"
    if num[0] == '9':
        word = "Nine"
    if num[0] != '0':
        word = word + " Hundred and "
    word = word + text
    word = word.strip()
    return word

def thousand(num):
    word = ''
    pref = ''
    text = ''
    length = len(num)
    if length == 6:
        text = hundred(num[3:])
        pref = hundred(num[:3])
    if length == 5:
        text = hundred(num[2:])
        pref = ten(num[:2])
    if length == 4:
        text = hundred(num[1:])
        if num[0] == '1':
            word = "One"
        if num[0] == '2':
            word = "Two"
        if num[0] == '3':
            word = "Three"
        if num[0] == '4':
            word = "Four"
        if num[0] == '5':
            word = "Five"
        if num[0] == '6':
            word = "Six"
        if num[0] == '7':
            word = "Seven"
        if num[0] == '8':
            word = "Eight"
        if num[0] == '9':
            word = "Nine"
        word = word + " Thousand "
    word = word + text
    if length == 6 or length == 5:
        word = pref + " Thousand " + word
    word = word.strip()
    return word

def word(num):
    num = str(num)
    len1 = len(num)
    if len1 == 1:
        return once(num)
    elif len1 == 2:
        return ten(num)
    elif len1 == 3:
        return hundred(num)
    elif num == "1000":
        return "one thousand"

x = "thousandand"
print(x[0:-3])

word1 = word(342).replace(" ","")
word1 = word1.replace("-","")
print(word1)
print(len(word1))

sum = 0
for num in range(1,1001):
    word1 = word(num).replace(" ","")
    word1 = word1.replace("-","")
    if word1[-3:] == "and":
        word1 = word1[0:-3]
    print(word1)
    sum += len(word1)

print(sum + 3)