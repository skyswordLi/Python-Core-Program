import os

ls = os.linesep;

fname = raw_input( "filename = " )
# get filenames
while True:
    if os.path.exists( fname ):
        print( "ERROR: %s already exits." % ( fname ) )
    else:
        break

# get file content (text) lines
all = []
print( "\nEnter lines ('.' by itself to quit)." )

# loop until user terminate input
while True:
    entry = raw_input( '>>>' )
    if entry == '.':
        break
    else:
        all.append( entry )

# write lines to file with proper line-ending
fobj = open( fname, 'w' )
fobj.writelines( ["%s%s" % ( x, ls ) for x in all] )
fobj.close()
print( "DONE!" )
