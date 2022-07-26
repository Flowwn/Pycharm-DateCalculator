import datetime

realTimeDate = [datetime.datetime.now().day, datetime.datetime.now().month, datetime.datetime.now().year]
realTimeYear = datetime.datetime.now().year

date = []

# Get and Check the year of the Input

year = int(input("Year: "))

if year >= datetime.datetime.now().year:
    date.append(year)
else:
    print("Input 'Year' can't be in the past!")
    exit()

isLeapYear = float(year / 4).is_integer() and not float(year / 100).is_integer()

if not isLeapYear:
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Get and Check the month of the Input
month = int(input("Month: "))

if 0 < month <= 12:
    date.append(month)
else:
    print("Input isn't in range of 1-12!")
    exit()


# Get and Check the day of the Input
day = int(input("Day: "))

if 0 < day <= months[month - 1]:
    date.append(day)
else:
    print("Input isn't in range of 1-" + months[month - 1].__str__() + "!")
    exit()


def CalculateDaysRange():

    leapYear = float(realTimeYear / 4).is_integer() and not float(realTimeYear / 100).is_integer()

    if not leapYear:
        _months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        _months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    days = 0
    currDay = realTimeDate[0]
    currMonth = realTimeDate[1]
    currYear = realTimeDate[2]

    while currDay != date[2] or currMonth != date[1] or currYear != date[0]:

        if currDay < _months[currMonth - 1]:
            currDay += 1
            days += 1
            # print("CurrDay: " + currDay.__str__())
        else:
            currDay = 0

            if currMonth >= 12:
                currMonth = 1
                currYear += 1

                leapYear = float(currYear / 4).is_integer() and not float(currYear / 100).is_integer()

                if not leapYear:
                    _months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                else:
                    _months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

            else:
                currMonth += 1
                # print("CurrMonth: " + currMonth.__str__())

    print("Days until " + date[0].__str__() + "." + date[1].__str__() + "." + date[2].__str__() + ": " + days.__str__())


CalculateDaysRange()

t = input()
