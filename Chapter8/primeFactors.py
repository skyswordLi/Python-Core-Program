import prime
import getFactors


def prime_factorization(num):
    factors = getFactors.get_factors(num)
    prime_factories = [i for i in factors[1:] if prime.is_prime(i)]
    result = []
    
    while num >= 1:
        for prime_number in prime_factories:
            if num % prime_number == 0:
                result.append(prime_number)
                break
        num //= prime_number

    return result

if '__main__' == __name__:
    print sorted(prime_factorization(9999))
