print "This script decide the grade of average score of 5 input courses' scores."

print "Please input your scores of 5 courses:"
totalCourseNum = 5
courseNum = 0
scores = []
while courseNum < totalCourseNum:
    score = int(raw_input('score = '))
    if score < 0 or score > 100:
        print "Input error, score must between 0 and 100."
        continue
    scores.append(score)
    courseNum += 1

averScore = sum(scores) / courseNum

print "Your grade will be:"
if 90 <= averScore <= 100:
    print 'A'
elif 80 <= averScore <= 89:
    print 'B'
elif 70 <= averScore <= 79:
    print 'C'
elif 60 <= averScore <= 69:
    print 'D'
elif 0 <= averScore < 60:
    print 'F'

