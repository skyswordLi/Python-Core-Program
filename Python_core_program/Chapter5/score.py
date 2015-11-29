def grade( score ):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score <= 89:
        return 'B'
    elif 70 <= score <= 79:
        return 'C'
    elif 60 <= score <= 69:
        return 'D'
    elif 0 <= score < 60:
        return 'F'
    else:
        return 'Wrong scroe input.'

print( "Please input your score to get the grade:" )
score = float( raw_input( 'score = ' ) )
print( 'Your grade will be %c' % grade( score ) )
