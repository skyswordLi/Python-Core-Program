def get_factors(num):
    assert(num > 0)
    factors = []
    for item in range(1, num + 1):
        if num % item == 0:
            factors.append(item)
    return factors

if '__main__' == __name__:
    print get_factors(100)
