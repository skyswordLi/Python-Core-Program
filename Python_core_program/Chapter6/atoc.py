def atoc( string ):
    length = len( string )

    pcnt = string.count( '+' )
    ncnt = string.count( '-' )
    assert 0 <= pcnt <= 2
    assert 0 <= ncnt <= 2

    if 'j' not in string:
        try:
            real = float( string )
            comp = 0
        except:
            print( 'Error convert string to float.' )
            return 'Wrong'
    else:
        assert string.endswith( 'j' )
        if pcnt == 2:
            pindex  = string.find( '+' )
            prindex = string.rfind( '+' )
            if pindex + 1 == prindex:
                assert pindex == 0
                real = 0
                if string[prindex + 1] == 'j':
                    comp = 1
                else:
                    comp = float( string[prindex + 1 : length - 1] )
            else:
                real = float( string[pindex + 1 : prindex] )
                comp = float( string[prindex + 1: length - 1] )
        elif ncnt == 2:
            pindex  = string.find( '-' )
            prindex = string.rfind( '-' )
            if pindex + 1 == prindex:
                assert pindex == 0
                real = 0
                if string[prindex + 1] == 'j':
                    comp = 1
                else:
                    comp = float( string[prindex: length - 1] )
            else:
                real = float( string[pindex: prindex] )
                comp = float( string[prindex: length - 1] )
        
    return complex( real, comp )
    
