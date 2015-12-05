def m2hm(minutes):
    '''This function change input minutes to corresponding hours + minutes'''
    hours = minutes // 60
    new_minutes = minutes - 60 * hours
    if hours == 0:
        if new_minutes == 1:
            time_str = str(new_minutes) + 'minute'
        else:
            time_str = str(new_minutes) + 'minutes'
    elif hours == 1:
        if new_minutes == 0:
            time_str = str(hours) + 'hour'
        elif new_minutes == 1:
            time_str = str(hours) + 'hour ' + str(new_minutes) + 'minute'
        else:
            time_str = str(hours) + 'hour ' + str(new_minutes) + 'minutes'
    else:
        if new_minutes == 0:
            time_str = str(hours) + 'hours'
        elif new_minutes == 1:
            time_str = str(hours) + 'hours ' + str(new_minutes) + 'minute'
        else:
            time_str = str(hours) + 'hours ' + str(new_minutes) + 'minutes'
    return time_str

print "Please input number of minutes to change, negative value or zero to end:"
while True:
    try:
        input_minutes = int(raw_input('minutes = '))
        if input_minutes <= 0:
            print "Thanks for testing. Bye"
            break
        else:
            print "The value you input is %d minute(s)" % input_minutes
            print "And after change it will be: %s" % m2hm(input_minutes)
    except TypeError:
        print "Wrong value input, must be an integer. "
        continue
