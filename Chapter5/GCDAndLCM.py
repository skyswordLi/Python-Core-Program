def gcd(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 % num1 == 0:
        return num1
    else:
        while num1 > 0:
            remain = num2 % num1
            num2 = num1
            num1 = remain
        return num2


def lcm(num1, num2):
    return num1 * num2 / gcd(num1, num2)


def main():
    print '''This program get the greatest common factor and the least common
    multiple of two numbers.'''
    number1 = int(raw_input('number1 = '))
    number2 = int(raw_input('number2 = '))
    gcd_value = gcd(number1, number2)
    lcm_value = lcm(number1, number2)
    print "The gcd and LCM of %d and %d are %d and %d." % (number1, number2, gcd_value, lcm_value)


main()
