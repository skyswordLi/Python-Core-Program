def upLowChange( myStr ):
    strlen    = len( myStr )
    outputStr = ''

    for i in range( strlen ):
        if myStr[ i ].isupper():
            outputStr += myStr[ i ].lower()
        elif myStr[ i ].islower():
            outputStr += myStr[ i ].upper()
        else:
            outputStr += myStr[ i ]

    return outputStr

if __name__ == "__main__":
    print( "Please input a string to change:" )
    inputStr = raw_input( 'inputStr = ' )
    print( "Before changed, the string is %s" % inputStr )
    outStr   = upLowChange( inputStr )
    print( "After changed, the string is %s" % outStr )
