def str2complex(string):
    real, comp = 0, 0
    length = len(string)

    plus_sign_count = string.count('+')
    minus_sign_count = string.count('-')
    assert 0 <= plus_sign_count <= 2
    assert 0 <= minus_sign_count <= 2

    if 'j' not in string:
        try:
            real = float(string)
            comp = 0
        except TypeError:
            print 'Error convert string to float.'
            return 'Wrong'
    else:
        assert string.endswith('j')
        if string[0] == '+' or string[0] == '-':
            assert()
        plus_sign_index = string.find('+')
        plus_sign_right_index = string.rfind('+')
        if plus_sign_index + 1 == plus_sign_right_index:
            assert plus_sign_index == 0
            real = 0
            if string[plus_sign_right_index + 1] == 'j':
                comp = 1
            else:
                comp = float(string[plus_sign_right_index + 1:length - 1])
        else:
            real = float(string[plus_sign_index + 1:plus_sign_right_index])
            comp = float(string[plus_sign_right_index + 1:length - 1])

        minus_sign_index = string.find('-')
        minus_sign_right_index = string.rfind('-')
        if minus_sign_index + 1 == minus_sign_right_index:
            assert minus_sign_index == 0
            real = 0
            if string[minus_sign_right_index + 1] == 'j':
                comp = 1
            else:
                comp = float(string[minus_sign_right_index:length - 1])
        else:
            real = float(string[minus_sign_index:minus_sign_right_index])
            comp = float(string[minus_sign_right_index:length - 1])
        
    return complex(real, comp)

print str2complex('1 + 2j')
