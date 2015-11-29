def GCD( num1, num2 ):
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 % num1 == 0:
        return num1
    else:
        while num1 > 0:
            remain = num2 % num1
            num2   = num1
            num1   = remain
        return num2

def LCM( num1, num2 ):
    return num1 * num2 / GCD( num1, num2 )

def main():
    print( '''This program get the greates common divisior and the least common
    muliple of two numbers.''' )
    number1 = int( raw_input( 'number1 = ' ) )
    number2 = int( raw_input( 'number2 = ' ) )
    gcd     = GCD( number1, number2 )
    lcm     = LCM( number1, number2 )
    print( "The GCD and LCM of %d and %d are %d and %d." % ( number1, number2, gcd, lcm ) )
