print( 'This program is used for copying contents of file1 to file2.' )
print( 'Please enter two file names to do copy.' )
file1 = raw_input( 'Please enter file1: ' )
file2 = raw_input( 'Please enter file2: ' )

try:
    with open( file1 ) as f1:
        try:
            with open( file2, 'w+' ) as f2:
                for line in f1:
                    f2.write( line )
        except Exception as e:
            print( type( e ) )
except Exception as e:
    print( e )

try:
    with open( file2 ) as f:
        print( f.read() )
except Exception as e:
    print( e )
    
