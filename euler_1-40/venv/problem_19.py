count = 0

# day 0  == monday, 6 == sunday
day = 5
date = 29
month = 12
year = 1900

while year < 2001:
    # increment
    day = (day + 1) % 7
    date += 1
    if month in [9,4,6,11] and date == 31: # 30 days
        date = 1
        month += 1

    elif month == 2 and date > 27: # 29, 28 on leap years
        # leap year
        if year % 4 == 0:
            if date == 30:
                date = 1
                month += 1
        # non leap year
        else:
            if date == 29:
                date = 1
                month += 1

    elif month in [1,3,5,7,8,10,12] and date == 32: #31 days
        date = 1
        month += 1

    if month == 13:
        month = 1
        year += 1
    if date == 1 and day == 6:
        count += 1
    print(day,date,month,year,date == 1 and day == 6)

print(count)