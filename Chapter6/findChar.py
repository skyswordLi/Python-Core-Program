def find_chr(string, char):
    length = len(string)
    i = 0
    while i < length:
        if string[i] == char:
            return i
        i += 1
    return -1


def right_find_chr(string, char):
    length = len(string)
    i = -1
    while i >= -length:
        if string[i] == char:
            return length + i
        i -= 1
    return -1


def sub_chr(string, original_char, new_char):
    length = len(string)
    i = 0
    while i < length:
        if string[i] == original_char:
            string = string[0:i] + new_char + string[i + 1:]
        i += 1
    return string
