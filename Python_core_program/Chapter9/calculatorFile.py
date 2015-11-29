import sys
import os

def new_eval( num ):
    if num[1] == '+':
        return float( num[0] ) + float( num[2] )
    elif num[1] == '-':
        return float( num[0] ) - float( num[2] )
    elif num[1] == '*':
        return float( num[0] ) * float( num[2] )
    elif num[1] == '/':
        try:
            return float( num[0] ) / float( num[2] )
        except Exception as e:
            print( e )
    elif num[1] == '//':
        try:
            return float( num[0] ) // float( num[2] )
        except Exception as e:
            print( e )
    elif num[1] == '%':
        try:
            return float( num[0] ) % float( num[2] )
        except Exception as e:
            print( e )
    elif num[1] == '**':
        return float( num[0] ) ** float( num[2] )
    else:
        print( 'Error operator' )
        return -1e-100
        

if __name__ == '__main__':
    agrv = sys.argv[1:]
    if agrv[0] == 'print':
        try:
            with open( 'result.txt' ) as f:
                print( f.read() )
            os.remove( 'result.txt' )
        except Exception as e:
            print( e )
    else:
        try:
            with open( 'result.txt', 'a+' ) as f:
                value = new_eval( agrv )
                if value != -1e-100:
                    f.write( ''.join( agrv ) )
                    f.write( '\n' )
                    f.write( str( value ) )
                    f.write( '\n' )
                    print( 'The result is %d' % value )
        except Exception as e:
            print( e )
