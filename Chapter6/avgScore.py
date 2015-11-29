def avgScore():
    scores = []

    print( "Input some scores to calculate average" )
    while True:
        try:
            score = float( raw_input( 'score = ' ) )
            scores.append( score )
        except:
            break
        if not len( scores ):
            return 0
        else:
            avg = sum( scores ) / len( scores )
    return avg
