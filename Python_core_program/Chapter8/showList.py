def showList( frm, to, increment ):
    assert( frm <= to )
    assert( increment >= 0 )
    item = frm
    while item <= to:
        if item + increment > to:
            print( item )
            break
        else:
            print( item, end = ',' )
            item += increment

showList( 2, 26, 4 )
