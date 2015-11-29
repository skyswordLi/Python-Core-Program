def leapYear( year ):
    return ( 0 == year % 4 and 0 != year % 100 or 0 == year % 400 )

print( "Please input a year to decide whether it's a leap year:" )
year = int( raw_input( 'year = ' ) )
if leapYear( year ):
    print( "Year %d is a leap year." % year )
else:
    print( "Year %d is not a leap year." % year )

