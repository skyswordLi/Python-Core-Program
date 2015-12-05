def show_str():
    input_str = raw_input('Input string:')
    lens = len(input_str)
    if lens == 0:
        return False
    if lens == 1:
        print input_str
        return True
    for i, j in enumerate(input_str):
        if i == 0 and len(input_str) != 1:
            print j, input_str[i + 1]
        elif i == len(input_str) - 1 and i != 0:
            print input_str[i - 1]
        else:
            print input_str[i - 1], j, input_str[i + 1]
    return True

