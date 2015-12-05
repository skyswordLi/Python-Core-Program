def avg_score():
    scores = []

    print "Input some scores to calculate average, negative value to end:"
    while True:
        try:
            score = float(raw_input('score = '))
            scores.append(score)
            if score < 0:
                break
        except TypeError:
            break
    if not scores:
        return 0
    else:
        avg = sum(scores) / len(scores)

    return avg

if '__main__' == __name__:
    print 'Your average score is %f' % avg_score()
