def prt_dec_bin_oct_hex_asc_str(n):
    print 'SAMPLE OUTPUT %d' % n
    print '-' * 15

    begin_str = raw_input('Enter begin value: ')
    end_str = raw_input('Enter end value: ')

    begin, end = int(begin_str), int(end_str)

    print '%-10s%-20s%-10s%-10s%-10s' % ('DEC', 'BIN', 'OCT', 'HEX', 'ASCII')
    print '-' * 40 

    for number in range(begin, end + 1):
        if number > 32:
            print '%-10s%-20s%-10s%-10s%-10s' % (number, bin(number)[0] + bin(number)[2:],
                                                 oct(number)[1:], hex(number)[2:], chr(number))
        else:
            print '%-10s%-20s%-10s%-10s%-10s' % (number, bin(number)[0] + bin(number)[2:], 
                                                 oct(number)[1:], hex(number)[2:], '')

if __name__ == '__main__':
    prt_dec_bin_oct_hex_asc_str(1)
    prt_dec_bin_oct_hex_asc_str(2)

