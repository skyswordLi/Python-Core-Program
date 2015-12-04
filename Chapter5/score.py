def grade(score):
    assert 0 <= score <= 100, 'Wrong input score!'
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    elif 0 <= score < 60:
        return 'F'

print "Please input your score to get the grade:"
your_score = float(raw_input('score = '))
print 'Your grade will be %s' % grade(your_score)
