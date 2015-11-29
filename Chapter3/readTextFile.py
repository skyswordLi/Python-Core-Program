# get filename
fname = raw_input( 'Enter filename:' )

print

# attempt to open file for reading
try:
    fobj = open( fname, 'r' )
except IOError:
    print( "*** file open error!" )
else:
    # display contents to screen
    for eachLine in fobj:
        print( eachLine )
    fobj.close()
