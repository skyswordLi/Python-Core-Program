def int2ip():
    ints = raw_input('ints = ')
    hexes = hex(int(ints))[2:]
    while len(hexes) < 8:
        hexes = '0' + hexes
    ip1 = int(hexes[0] + hexes[1], 16)
    ip2 = int(hexes[2] + hexes[3], 16)
    ip3 = int(hexes[4] + hexes[5], 16)
    ip4 = int(hexes[6] + hexes[7], 16)

    return '%03d.%03d.%03d.%03d' % (ip1, ip2, ip3, ip4)


def ip2int():
    ip = raw_input('ip = ')
    ips = ip.split('.')
    ip = []
    for i in range(0, 4):
        ip.append(int(ips[i]))
        ip[i] = hex(ip[i])[2:]
        if len(ip[i]) == 1:
            ip[i] = '0' + ip[i]
    return int(ip[0] + ip[1] + ip[2] + ip[3], 16)
