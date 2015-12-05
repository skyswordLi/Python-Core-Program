def show_list(frm, to, increment):
    assert(frm <= to), 'from value should smaller than to value'
    assert(increment >= 0), 'increment should be positive'
    item = frm
    while item <= to:
        if item + increment > to:
            print item
            break
        else:
            print item,
            item += increment

show_list(2, 26, 4)
