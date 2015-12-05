def is_perfect(num):
    factors = [i for i in range(1, num // 2 + 1) if num % i == 0]
    return sum(factors) == num

if __name__ == '__main__':
    print "please input value between 0 to 100000 to test:"
    while True:
        input_num = int(raw_input("input_num = "))
        if 0 < input_num < 100000:
            if is_perfect(input_num):
                print "%d is a perfect integer" % input_num
            else:
                print "%d is not a perfect integer" % input_num
        else:
            print "Thank you for testing. Bye!"
            break
