import math


def is_prime(number):
    if number < 2:
        print "The number is not correct, should be larger than 1"
        return False
    else:
        for i in range(2, int(math.sqrt(number) + 1)):
            if number % i == 0:
                return False
        return True

if '__main__' == __name__:
    for num in range(2, 100):
        if is_prime(num):
            print "%d is a prime number" % num
        else:
            print "%d is not a prime number" % num
