fileName = raw_input( 'Enter file name:' )
fobj     = open( fileName, 'r' )
for eachLine in fobj:
    print( eachLine )
fobj.close()
