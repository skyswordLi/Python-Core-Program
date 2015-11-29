def findchar( myStr, myChar ):
    '''This function return the first time( index ) a char appears in the given string.
    If the given char letter cannot be found in the string, return -1 else return
    the first index.'''

    strLen = len( myStr )
    for i in range( strLen ):
        if myStr[ i ] == myChar:
            return i
    return -1

def rfindchar( myStr, myChar ):
    '''This function return the last time( right index ) a char appears in the given string.
    If the given char letter cannot be found in the string, return -1 else return
    the first index.'''

    strLen = len( myStr )
    for i in range( strLen ):
        if myStr[ -1 - i ] == myChar:
            return strLen - i
    return -1

def subchr( myStr, myChar, myNewChar ):
    '''This function replace all myChar to myNewChar and return the new string.'''

    outStr = ''
    strLen = len( myStr )
    for i in range( strLen ):
        if myStr[ i ] == myChar:
            outStr += myNewChar
        else:
            outStr += myStr[ i ]
    return outStr

if __name__ == "__main__":
    print( "Please input a string and a char to find:" )
    inputStr     = raw_input( 'inputStr  = ' )
    inputChar    = raw_input( 'inputChar = ' )
    inputNewChar = raw_input( 'inputNewChar = ' )

    fIndex    = findchar(  inputStr, inputChar )
    if fIndex != -1:
        print( 'The first index of the given char of the given string is %d ' % ( fIndex ) )
    else:
        print( 'Cannot find the given char in the given string.' )

    lIndex    = rfindchar( inputStr, inputChar )
    if lIndex != -1:
        print( 'The last index of the given char of the given string is %d ' % ( lIndex ) )
    else:
        print( 'Cannot find the given char in the given string.' )

    outStr = subchr( inputStr, inputChar, inputNewChar )
    print( 'The new string is %s' % ( outStr ) )

