def m2hm( minutes ):
    '''This function change input minutes to corresponding hours + minutes'''
    hours       = minutes // 60
    new_minutes = minutes - 60 * hours
    if hours == 0:
        if new_minutes == 1:
            timeStr = str( new_minutes ) + 'minute'
        else:
            timeStr = str( new_minutes ) + 'minutes'
    elif hours == 1:
        if new_minutes == 0:
            timeStr = str( hours ) + 'hour'
        elif new_minutes == 1:
            timeStr = str( hours ) + 'hour ' + str( new_minutes ) + 'minute'
        else:
            timeStr = str( hours ) + 'hour ' + str( new_minutes ) + 'minutes'
    else:
        if new_minutes == 0:
            timeStr = str( hours ) + 'hours'
        elif new_minutes == 1:
            timeStr = str( hours ) + 'hours ' + str( new_minutes ) + 'minute'
        else:
            timeStr = str( hours ) + 'hours ' + str( new_minutes ) + 'minutes'
    return timeStr

print( "Please input number of minutes to change, negative value or zero to end:" )
while True:
    try:
        minutes = int( raw_input( 'minutes = ' ) )
        if minutes <= 0:
            print( "Thanks for testing. Bye" )
            break
        else:
            print( "The value you input is %d minute(s)" % minutes )
            print( "And after change it will be: %s" % m2hm( minutes ) )
    except:
        print( "Wrong value input, must be an integer. ")
        continue
