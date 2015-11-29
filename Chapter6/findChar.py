def findchr( string, char ):
    length = len( string )
    i = 0
    while i < length:
        if string[i] == char:
            return i
        i += 1
    return -1

def rfindchr( string, char ):
    length = len( string )
    i = -1
    while i >= -length:
        if string[i] == char:
            return length + i
        i -= 1
    return -1

def subchr( string, origchar, newchar ):
    length = len( string )
    i = 0
    while i < length:
        if string[i] == origchar:
            string = string[0:i] + newchar + string[i + 1:]
        i += 1
    return string
    
