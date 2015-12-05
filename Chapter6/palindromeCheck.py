import sys


def palindrome(input_str):
    str_len = len(input_str)
    if str_len % 2 == 0:
        middle = str_len // 2 - 1
    else:
        middle = str_len // 2

    for i in range(middle + 1):
        if input_str[i] == input_str[-1 - i]:
            pass
        else:
            print "It's not a palindrome."
            sys.exit()
    print "It's a palindrome."

if __name__ == "__main__":
    myStr = raw_input('myStr = ')
    palindrome(myStr)
