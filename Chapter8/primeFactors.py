import prime
import getFactors

def primeFactorization( num ):
    factors = getFactors.getFactors( num )
    primeFactoriers = [i for i in factors[1:] if prime.isPrime( i )]
    result = []
    
    while num >= 1:
        for primeNumber in primeFactoriers:
            if num % primeNumber == 0:
                result.append( primeNumber )
                break
        num //= primeNumber

    return result

if '__main__' == __name__:
    print( sorted( primeFactorization( 1000 ) ) )
