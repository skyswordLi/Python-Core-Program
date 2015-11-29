def sortedNumbers( inputList ):
    numList = []
    for item in inputList:
        numList.append( int( item ) )
    return sorted( numList, reverse = True )

def sortedNumbersDictOrder( inputList ):
    newList = []
    for item in inputList:
        newList.append( str( item ) )
    newList = sorted( newList, reverse = True )
    for i, x in enumerate( newList ):
        newList[i] = x
    return newList