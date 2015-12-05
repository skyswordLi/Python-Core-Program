def tr(src_str, dst_str, string, sensitive):
    lens = len(src_str)
    src, dst, my_str = src_str, dst_str, string

    if not sensitive:
        src, dst, str1 = src_str.lower(), dst.lower(), my_str.lower()
    while True:
        index = my_str.find(src)
        if index > -1:
            string = string[0:index] + dst_str + string[index + lens:]
            if not sensitive:
                my_str = my_str[0:index ] + dst + my_str[index + lens:]
            else:
                my_str = string
        else:
            break
    return string
