import math

def isPrime( num ):
    if num < 2:
        print( "The number is not correct, should be larger than 1" )
        return False
    else:
        for i in range( 2, int( math.sqrt( num ) + 1 ) ):
            if num % i == 0:
                return False
        return True

if '__main__' == __name__:
    for num in range( 2, 100 ):
        if isPrime( num ):
            print( "%d is a prime number" % num )
        else:
            print( "%d is not a prime number" % num )
