import string

uppers = string.ascii_uppercase
lowers = string.ascii_lowercase

encryptNum = 13
letterCount = 26

def dencrypt( str2encrypt ):
    strEncrypted = ''

    for letter in str2encrypt:
        if letter.isupper():
            letter = uppers[( uppers.index( letter ) + encryptNum ) % letterCount]
        elif letter.islower():
            letter = lowers[( lowers.index( letter ) + encryptNum ) % letterCount]
        strEncrypted += letter
    return strEncrypted

if '__main__' == __name__:
    print( 'This program can encrypt your input string and also decrypt the ' \
           + 'string that encrypted, please enjoy it!' )
    print( 'Please input any string( \'finish\' to end ) to test' )
    while True:
        stringToDencrypt = raw_input( 'stringToDencrypt = ' )
        if stringToDencrypt != 'finish':
            stringEncrypted = dencrypt( stringToDencrypt )
            print( 'Atter encrypted, the string you input became \'%s\'' % stringEncrypted )
            stringDecrypted = dencrypt( stringEncrypted )
            print( 'Atter decrypted, the string that encrypted became \'%s\'' % stringDecrypted )
            print( 'Plese input next string:' )
        else:
            print( 'Thanks for testing, bye!' )
            break
    
