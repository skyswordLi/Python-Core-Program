import datetime

def diffDates( dateString1, dateString2 ):
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date1 = dateString1.split( '/' )
    year1, month1, day1 = int( date1[0] ), int( date1[1] ), int( date1[2] )

    date2 = dateString2.split( '/' )
    year2, month2, day2 = int( date2[0] ), int( date2[1] ), int( date2[2] )

    diff = ( year2 - year1 ) * 365 + day2 - day1

    leapNum = len( [year for year in range( min( year1, year2 ), max( year1, year2 ) ) \
            if ( 0 == year % 4 and 0 != year % 100 ) or 0 == year % 400] )

    if year1 <= year2:
        diff += leapNum
    else:
        diff -= leapNum

    if month1 <= month2:
        for month in range( month1, month2 ):
            diff += monthDays[month - 1]
    else:
        month1, month2 = month2, month1
        for month in range( month1, month2 ):
            diff -= monthDays[month - 1]

    return abs( diff )

def daysFromBirth( birthday ):
    return diffDates( birthday, nowDateString )

def daysToNextBirth( birthday ):
    nextBirth = str( int( now[0 : 4] ) + 1 ) + birthday[4 :]
    return diffDates( nowDateString, nextBirth )

now = str( datetime.datetime.now() )
nowDateString = now[0 : 4] + '/' + now[5 : 7] + '/' + now[8 : 10]

print( "Please give your choice( 1, 2, 3)to compute what you want(-1 to quit):" )
while True:
    choice = int( raw_input( "choice = " ) )

    if 1 == choice:
        print( "Please input two date strings as YYYY/MM/DD format:" )
        date1 = input( "date1 = " )
        date2 = input( "date2 = " )
        print( "The difference between the two days you in put is %d" % diffDates( date1, date2 ) )

    elif 2 == choice:
        print( "Please input your birthday as format YYYY/MM/DD:" )
        birthday = input( "birthday = " )
        print( "Till now, there are %d days from your birthday" % daysFromBirth( birthday ) )

    elif 3 == choice:
        print( "Please input your birthday as format YYYY/MM/DD:" )
        birthday = input( "birthday = " )
        print( "There are %d days from now to your next birthday" % daysToNextBirth( birthday ) )

    elif -1 == choice:
        print( "Thanks for using, bye!" )
        break
