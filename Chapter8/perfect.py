def isPerfect( num ):
    factors = [i for i in range( 1, num // 2 + 1 ) if num % i == 0]
    return sum( factors ) == num

if __name__ == '__main__':
    print( "please input value to test:(non negative value to end)" )
    while True:
        num = int( raw_input( "num = " ) )
        if num > 0:
            if isPerfect( num ):
                print( "%d is a perfect integer" % num )
            else:
                print( "%d is not a perfect integer" % num )
        else:
            print( "Thank you for testing. Bye!" )
            break
