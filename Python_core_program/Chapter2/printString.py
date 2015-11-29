print( "Please enter a string to print:" )
string = raw_input( "string = " )

i      = 0
strlen = len( string )

print( "Following are while loop print results:" )
while i < strlen:
    print( string[i] )
    i += 1

print( "Following are for loop print results:" )
for i in range( strlen ):
    print( string[i] )
