import string

Letters = string.ascii_uppercase
letters = string.ascii_lowercase


def upper_lower_change(input_str):
    new_str = ''
    for item in input_str:
        if item in Letters:
            index = Letters.index(item)
            item = letters[index]
        elif item in letters:
            index = letters.index(item)
            item = Letters[index]
        new_str += item
    return new_str

print "Please in put a string to change:"
myStr = raw_input('myStr = ')
print upper_lower_change(myStr)
