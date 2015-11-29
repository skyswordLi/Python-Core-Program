import sys

def palindrome( inputStr ):
    strLen = len( inputStr )
    if strLen % 2 == 0:
        middle = strLen // 2 - 1
    else:
        middle = strLen // 2

    for i in range( middle + 1 ):
        if inputStr[ i ] == inputStr[ -1 - i ]:
            pass
        else:
            print( "It's not a palindrome." )
            sys.exit()
    print( "It's a palindrome." )

if __name__ == "__main__":
    myStr = raw_input( 'myStr = ' )
    palindrome( myStr )
