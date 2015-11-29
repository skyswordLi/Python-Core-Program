print( "This script generates N random numbers whose values are between 0 ~ 2 ^ 31 - 1." )
import random
N = random.randint( 1, 100 )
array = []

for i in range( N ):
    rand = random.randrange( 1, 2 ** 31 - 1 )
    array.append( rand )
print( "The generated array which has %d elements is:" % ( N ) )
print( array )
print( "\n" )

M = random.randint( 1, N )
randomArray = []
for i in range( M ):
    element = random.choice( array )
    randomArray.append( element )
print( "After randomly choose %d elements of array, the sorted new random array is." % ( M ) )
print( sorted( randomArray ) )
