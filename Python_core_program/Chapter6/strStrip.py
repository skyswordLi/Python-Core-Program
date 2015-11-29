def strStrip( inputStr ):
    "Remove spaces at begin or end of input string." 

    inputStrLen  = len( inputStr )
    i            = 0
    while i < inputStrLen:
        if inputStr[0] == ' ' or inputStr[0] == '\t' or inputStr[0] == '\n':
            inputStr = inputStr[1 : ]
        else:
            break

    inputStrLen = len( inputStr )
    while i < inputStrLen:
        if inputStr[-1 + i] == ' ' or inputStr[-1 + i] == '\t' or inputStr[-1 + i] == '\n':
            inputStr = inputStr[i : -1]
        else:
            break
    return inputStr

if __name__ == "__main__":
    myStr = '\n\t I Love Qin.    '
    print( myStr )
    print( "The striped string is %s" % strStrip( myStr ) )
