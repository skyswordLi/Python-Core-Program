def str_strip(input_str):
    input_str_length  = len(input_str)
    i = 0
    while i < input_str_length:
        if input_str[0] == ' ' or input_str[0] == '\t' or input_str[0] == '\n':
            input_str = input_str[1:]
        else:
            break

    input_str_length = len(input_str)
    while i < input_str_length:
        if input_str[-1 + i] == ' ' or input_str[-1 + i] == '\t' or input_str[-1 + i] == '\n':
            input_str = input_str[i:-1]
        else:
            break
    return input_str

if __name__ == "__main__":
    myStr = '\n\t I Love Qin.    '
    print myStr
    print "The striped string is\n %s" % str_strip(myStr)
