def showStr():
    istr = raw_input( 'Input string:' )
    lens = len( istr )
    if lens == 0:
        return False
    if lens == 1:
        print( istr )
        return True
    for i, j in enumerate( istr ):
        if i == 0 and len( istr ) != 1:
            print( j, istr[i + 1] )
        elif i == len( istr ) - 1 and i != 0:
            print( istr[i - 1] )
        else:
            print( istr[i - 1], j, istr[i + 1] )
    return True
