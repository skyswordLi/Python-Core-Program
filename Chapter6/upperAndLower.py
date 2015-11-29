import string

Letters = string.ascii_uppercase;
letters = string.ascii_lowercase;

def upperLower( str ):
    newStr = ''
    for item in str:
        if item in Letters:
            index = Letters.index( item )
            item  = letters[index]
        elif item in letters:
            index = letters.index( item )
            item  = Letters[index]
        newStr += item
    return newStr

print( "Please in put a string to change:" )
myStr = raw_input( 'myStr = ' )
print( upperLower( myStr ) )
