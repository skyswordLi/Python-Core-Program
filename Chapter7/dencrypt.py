import string

uppers = string.ascii_uppercase
lowers = string.ascii_lowercase

encryptNum = 13
letterCount = 26


def decrypt(str2encrypt):
    str_encrypted = ''

    for letter in str2encrypt:
        if letter.isupper():
            letter = uppers[(uppers.index(letter) + encryptNum) % letterCount]
        elif letter.islower():
            letter = lowers[(lowers.index(letter) + encryptNum) % letterCount]
        str_encrypted += letter
    return str_encrypted

if '__main__' == __name__:
    print 'This program can encrypt your input string and also decrypt the '\
          + 'string that encrypted, please enjoy it!'
    print 'Please input any string( \'finish\' to end ) to test'
    while True:
        stringToDecrypt = raw_input('stringToDecrypt = ')
        if stringToDecrypt != 'finish':
            stringEncrypted = decrypt(stringToDecrypt)
            print 'After encrypted, the string you input became \'%s\'' % stringEncrypted
            stringDecrypted = decrypt(stringEncrypted)
            print 'After decrypted, the string that encrypted became \'%s\'' % stringDecrypted
            print 'Please input next string:'
        else:
            print 'Thanks for testing, bye!'
            break
