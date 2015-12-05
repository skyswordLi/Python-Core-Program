import datetime


def diff_dates(date_str1, date_str2):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date1 = date_str1.split('/')
    year1, month1, day1 = int(date1[0]), int(date1[1]), int(date1[2])

    date2 = date_str2.split('/')
    year2, month2, day2 = int(date2[0]), int(date2[1]), int(date2[2])

    diff = (year2 - year1) * 365 + day2 - day1

    leap_num = len([year for year in range(min(year1, year2), max(year1, year2))
                    if (0 == year % 4 and 0 != year % 100) or 0 == year % 400])

    if year1 <= year2:
        diff += leap_num
    else:
        diff -= leap_num

    if month1 <= month2:
        for month in range(month1, month2):
            diff += month_days[month - 1]
    else:
        month1, month2 = month2, month1
        for month in range(month1, month2):
            diff -= month_days[month - 1]

    return abs(diff)


def days_from_birth(birthday):
    return diff_dates(birthday, nowDateString)


def days_to_next_birth(birthday):
    next_birth = str(int(now[0:4]) + 1) + birthday[4:]
    return diff_dates(nowDateString, next_birth)

now = str(datetime.datetime.now())
nowDateString = now[0:4] + '/' + now[5:7] + '/' + now[8:10]

print "Please give your choice(1, 2, 3)to compute what you want(-1 to quit):\n" \
      "1 means you want to compute the difference between two days you input\n" \
      "2 means you want to compute how many days have passed from your last birthday\n" \
      "3 means you want to compute how long it will take to reach your next birthday\n"
while True:
    choice = int(raw_input("choice = "))

    if 1 == choice:
        print "Please input two date strings as YYYY/MM/DD format:"
        input_date1 = raw_input("date1 = ")
        input_date2 = raw_input("date2 = ")
        print "The difference between the two days you in put is %d" % diff_dates(input_date1, input_date2)

    elif 2 == choice:
        print "Please input your birthday as format YYYY/MM/DD:"
        my_birthday = raw_input("my_birthday = ")
        print "Till now, there are %d days from your birthday" % days_from_birth(my_birthday)

    elif 3 == choice:
        print "Please input your birthday as format YYYY/MM/DD:"
        my_birthday = raw_input("my_birthday = ")
        print "There are %d days from now to your next birthday" % days_to_next_birth(my_birthday)

    elif -1 == choice:
        print "Thanks for using, bye!"
        break
