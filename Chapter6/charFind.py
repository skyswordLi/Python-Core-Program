def find_char(my_str, my_char):
    '''This function return the first time( index ) a char appears in the given string.
    If the given char letter cannot be found in the string, return -1 else return
    the first index.'''

    str_len = len(my_str)
    for i in range(str_len):
        if my_str[i] == my_char:
            return i
    return -1


def right_find_char(my_str, my_char):
    '''This function return the last time( right index ) a char appears in the given string.
    If the given char letter cannot be found in the string, return -1 else return
    the first index.'''

    str_len = len(my_str)
    for i in range(str_len):
        if my_str[-1 - i] == my_char:
            return str_len - i
    return -1


def sub_chr(my_str, my_char, my_new_char):
    '''This function replace all my_char to myNewChar and return the new string.'''

    out_str = ''
    str_len = len(my_str)
    for i in range(str_len):
        if my_str[i] == my_char:
            out_str += my_new_char
        else:
            out_str += my_str[i]
    return out_str

if __name__ == "__main__":
    print "Please input a string and a char to find:"
    inputStr = raw_input('inputStr  = ')
    inputChar = raw_input('inputChar = ')
    inputNewChar = raw_input('inputNewChar = ')

    fIndex = find_char(inputStr, inputChar)
    if fIndex != -1:
        print 'The first index of the given char of the given string is %d ' % fIndex
    else:
        print 'Cannot find the given char in the given string.'

    lIndex = right_find_char(inputStr, inputChar)
    if lIndex != -1:
        print 'The last index of the given char of the given string is %d ' % lIndex
    else:
        print 'Cannot find the given char in the given string.'

    outStr = sub_chr(inputStr, inputChar, inputNewChar)
    print 'The new string is %s' % outStr
