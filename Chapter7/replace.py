def tr( srcstr, dststr, string, sensitive ):
    lens = len( srcstr )
    src, dst, stri = srcstr, dststr, string

    if not sensitive:
        src, dst, str1 = srcstr.lower(), dst.lower(), stri.lower()
    while True:
        index = stri.find( src )
        if index > -1:
            string = string[ 0 : index ] + dststr + string[ index + lens : ]
            if not sensitive:
                stri = stri[ 0 : index ] + dst + stri[ index + lens : ]
            else:
                stri = string
        else:
            break
    return string
