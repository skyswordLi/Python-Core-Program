def upper_lower_change(my_str):
    str_len = len(my_str)
    output_str = ''

    for i in range(str_len):
        if my_str[i].isupper():
            output_str += my_str[i].lower()
        elif my_str[i].islower():
            output_str += my_str[i].upper()
        else:
            output_str += my_str[i]

    return output_str

if __name__ == "__main__":
    print "Please input a string to change:"
    inputStr = raw_input('inputStr = ')
    print "Before changed, the string is %s" % inputStr
    outStr = upper_lower_change(inputStr)
    print "After changed, the string is %s" % outStr
