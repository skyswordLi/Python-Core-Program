def printDBOHA( N ):
    print( 'SAMPLE OUTPUT %d' % N )
    print( '-' * 15 )

    beginStr = raw_input( 'Enter begin value: ' )
    endStr   = raw_input( 'Enter end value: ' )

    begin, end = int( beginStr ), int( endStr )

    print( '%-10s%-20s%-10s%-10s%-10s' % ( 'DEC', 'BIN', 'OCT', 'HEX', 'ASCII' ) )
    print( '-' * 40 )

    for number in range( begin, end + 1 ):
        if number > 32:
            print( '%-10s%-20s%-10s%-10s%-10s' % ( number, bin( number )[0] + bin( number )[2:], \
                oct( number )[1:], hex( number )[2:], chr( number ) ) )
        else:
            print( '%-10s%-20s%-10s%-10s%-10s' % ( number, bin( number )[0] + bin( number )[2:], \
                oct( number )[1:], hex( number )[2:], '' ) )

if __name__ == '__main__':
    printDBOHA( 1 )
    printDBOHA( 2 )

