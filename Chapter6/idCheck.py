def idcheck( myInput ):
    import string
    import keyword

    alphas = string.ascii_letters + '_'
    nums   = string.digits
    klist  = keyword.kwlist

    if myInput == 'stop':
        return True
    if myInput in klist:
        print( "No, it's a keyword, cannot be an identifier." )
        return False
    else:
        if myInput[0] not in alphas:
            print( "No, it's not a identifier. Identifier must start with a letter or _." )
            return False
        else:
            for otherLetters in myInput:
                if otherLetters not in alphas + nums:
                    print( "No, it's not a identifier. Identifier must only has letters or digits or _." )
                    return False
    return True

def main():
    print( "Welcome to the identifier checker, enter 'stop' to stop testing!" )
    while True:
        myInput = raw_input( 'Identifier to test:' )
        if True == idcheck( myInput ):
            if 'stop' == myInput:
                print( "Yes, it's a identifier and bye." )
                break
            else:
                print( "Yes, it's a identifier." )
