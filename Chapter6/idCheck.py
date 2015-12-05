def id_check(my_input):
    import string
    import keyword

    alphas = string.ascii_letters + '_'
    nums = string.digits
    key_list = keyword.kwlist

    if my_input == 'stop':
        return True
    if my_input in key_list:
        print "No, it's a keyword, cannot be an identifier."
        return False
    else:
        if my_input[0] not in alphas:
            print "No, it's not a identifier. Identifier must start with a letter or _."
            return False
        else:
            for otherLetters in my_input:
                if otherLetters not in alphas + nums:
                    print "No, it's not a identifier. Identifier must only has letters or digits or _."
                    return False
    return True


def main():
    print "Welcome to the identifier checker, enter 'stop' to stop testing!"
    while True:
        my_input = raw_input('Identifier to test:')
        if id_check(my_input):
            if 'stop' == my_input:
                print "Yes, it's a identifier and bye."
                break
            else:
                print "Yes, it's a identifier."

main()
