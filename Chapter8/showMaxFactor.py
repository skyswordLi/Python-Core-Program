def show_max_factor(num):
    assert(num >= 2), 'number should not be smaller than 2'
    count = num // 2
    while count > 1:
        if num % count == 0:
            print 'Largest factor of %d is %d' % (num, count)
            break
        count -= 1
    else:
        print '%d is prime' % num

for eachNum in range(2, 20):
    show_max_factor(eachNum)
