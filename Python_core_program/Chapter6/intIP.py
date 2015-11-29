def int2ip():
    ints = raw_input( 'ints = ' )
    hexs = hex( int( ints ) )[2:]
    while len( hexs ) < 8:
        hexs = '0' + hexs
    ip1 = int( hexs[0] + hexs[1], 16 )
    ip2 = int( hexs[2] + hexs[3], 16 )
    ip3 = int( hexs[4] + hexs[5], 16 )
    ip4 = int( hexs[6] + hexs[7], 16 )

    return '%03d.%03d.%03d.%03d' % ( ip1, ip2, ip3, ip4 )

def ip2int():
    ip  = raw_input( 'ip = ' )
    ips = ip.split( '.' )
    ip  = []
    for i in range( 0, 4 ):
        ip.append( int( ips[i] ) )
        ip[i] = hex( ip[i] )[2:]
        if len( ip[i] ) == 1:
            ip[i] = '0' + ip[i]
    return int( ip[0] + ip[1] + ip[2] + ip[3], 16 )
                   
