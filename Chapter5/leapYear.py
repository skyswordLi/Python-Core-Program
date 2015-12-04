def leap_year(year):
    return 0 == year % 4 and 0 != year % 100 or 0 == year % 400

print "Please input a year to decide whether it's a leap year:"
inputYear = int(raw_input('year = '))
if leap_year(inputYear):
    print "Year %d is a leap year." % inputYear
else:
    print "Year %d is not a leap year." % inputYear
