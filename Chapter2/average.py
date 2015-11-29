print( "This script computes the average value of some input values." )

print( "Please enter how many values you wanna compute:" )
NUM = int( input( "NUM = " ) )
array = []
print( "Please enter these values:" )
for i in range( NUM ):
    value = float( input( "value = " ) )
    array.append( value )

average = sum( array ) / NUM
print( "Average is %f" % ( average ) )
